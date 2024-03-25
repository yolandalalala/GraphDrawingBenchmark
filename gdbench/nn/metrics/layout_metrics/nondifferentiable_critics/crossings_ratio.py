from gdbench.constants import EPS
from gdbench.data import GraphStruct
from gdbench.nn.ops import EdgesIntersect
from .crossings import Crossings
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch.nn.functional as F
import torch_scatter


@CompositeMetric.register_metric("xingratio")
class CrossingsRatio(Crossings):

    def __init__(self, *, eps: float = EPS, batch_reduce: Optional[str] = "mean"):
        super().__init__(eps=eps, batch_reduce=batch_reduce)

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        return super().compute(layout) / layout.m.square().sum()
