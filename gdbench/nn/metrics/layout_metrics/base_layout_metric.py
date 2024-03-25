from gdbench.data import GraphStruct
from ...batch_operation import BatchOperation

from abc import abstractmethod

import torch


class BaseLayoutMetric(BatchOperation):

    @abstractmethod
    def compute(self, layout: GraphStruct) -> torch.Tensor:
        return NotImplemented
