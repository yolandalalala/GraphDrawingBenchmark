from .base_adverserial_criterion import BaseAdverserialCriterion

from typing import Optional

import torch
from torch import nn


class SGANCriterion(BaseAdverserialCriterion):

    def __init__(self, *, batch_reduce: Optional[str] = "mean"):
        super().__init__(batch_reduce=batch_reduce)

    def compute(self, encourage: torch.Tensor, discourage: torch.Tensor) -> torch.Tensor:
        return NotImplemented
