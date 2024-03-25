from gdbench.constants import EPS
from ..batch_operation import BatchOperation

from typing import Optional

import torch
from torch import nn


class SPC(BatchOperation):

    def __init__(self, *, batch_reduce: Optional[str] = "mean", eps: float = EPS):
        super().__init__(batch_reduce=batch_reduce)
        self.eps = eps

    def compute(self, value: torch.Tensor, reference: torch.Tensor) -> torch.Tensor:
        return (value - reference) / torch.maximum(value + self.eps, reference + self.eps)
