from gdbench.data import GraphStruct
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric
from ...jaccard_index import JaccardIndex

from typing import Optional

import torch


@CompositeMetric.register_metric("gabrial")
class GabrialJaccardDistance(BaseLayoutMetric):

    def __init__(self, *, batch_reduce: Optional[str] = "mean"):
        super().__init__(batch_reduce=batch_reduce)
        self.jaccard = JaccardIndex(batch_reduce=None)

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        return 1 - self.jaccard(layout.edge_index, layout.gabrial_index, batch_index=layout.batch)
