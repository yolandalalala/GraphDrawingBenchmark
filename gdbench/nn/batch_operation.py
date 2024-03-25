from .ops import Reduce

from typing import Optional
from abc import ABC, abstractmethod

import torch
from torch import nn


class BatchOperation(nn.Module, ABC):

    def __init__(self, *, batch_reduce: Optional[str] = "mean"):
        super().__init__()
        self.reduce: Reduce = Reduce(method=batch_reduce)

    @abstractmethod
    def compute(self, *args, **kwargs) -> torch.Tensor:
        return NotImplemented

    def forward(self, *args, **kwargs) -> torch.Tensor:
        return self.reduce(self.compute(*args, **kwargs))
