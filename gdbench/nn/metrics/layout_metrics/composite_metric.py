from gdbench.data import GraphStruct
from .base_layout_metric import BaseLayoutMetric

from typing import Optional, Callable, TypeVar, Dict, Type
from typing_extensions import Self

import torch

_Critic = TypeVar("_Critic", bound=BaseLayoutMetric)
_CriticCls = Type[_Critic]
_PresetFunc = Callable[..., Dict[str, float]]


class CompositeMetric(BaseLayoutMetric):

    _critic_registry: Dict[str, _Critic] = {}
    _preset_registry: Dict[str, Dict[str, float]] = {}

    @classmethod
    def register_metric(cls, _name: str, /, *args, **kwargs) -> Callable[[_CriticCls], _CriticCls]:
        def decorator(critic_cls: _CriticCls) -> _CriticCls:
            cls._critic_registry[_name] = critic_cls(*args, **kwargs, batch_reduce=None)
            return critic_cls
        return decorator

    @classmethod
    def register_preset(cls, _name: str, /, *args, **kwargs) -> Callable[[_PresetFunc], _PresetFunc]:
        def decorator(preset_func: _PresetFunc) -> _PresetFunc:
            cls._preset_registry[_name] = preset_func(*args, **kwargs)
            return preset_func
        return decorator

    @classmethod
    def get_preset(cls, preset: str) -> Dict[str, float]:
        return cls._preset_registry[preset]

    @classmethod
    def from_preset(cls, preset: str, *, batch_reduce: Optional[str] = "mean") -> Self:
        return cls(criteria_weights=cls._preset_registry[preset],
                   batch_reduce=batch_reduce)

    def __init__(self, *,
                 criteria_weights: Dict[str, float],
                 batch_reduce: Optional[str] = "mean"):
        super().__init__(batch_reduce=batch_reduce)
        self.weights: Dict[str, float] = criteria_weights
        self.cached_scores = {key: None for key in self.weights}

    def _cache_scores(self, layout: GraphStruct):
        for criterion in self.cached_scores:
            self.cached_scores[criterion] = self._critic_registry[criterion](layout)

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        self._cache_scores(layout)
        scores = [self.cached_scores[criterion] * self.weights[criterion]
                  for criterion in self.weights]
        return sum(scores)

    def get_raw_scores(self):
        return {
            criterion: self.reduce(score)
            for criterion, score in self.cached_scores.items()
        }


@CompositeMetric.register_preset("stress_only")
def stress_only() -> Dict[str, float]:
    return {
        'stress': 1.
    }


@CompositeMetric.register_preset("human_preference")
def human_preference() -> Dict[str, float]:
    return {
        'stress': 0.00029434361190166397,
        'xing': 0.0007957665417401572,
        'xangle': 0.0030477412542927345,
        'iangle': 0.0006086161066274451,
        'ring': 0.0003978516063712987,
        'absedge': 0.5699997020454531,
        'tsne': 0.4248559788336135,
    }
