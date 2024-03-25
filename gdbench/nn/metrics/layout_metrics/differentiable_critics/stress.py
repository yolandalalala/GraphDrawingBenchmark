from gdbench.data import GraphStruct
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch_scatter


# TODO: scale invariance
@CompositeMetric.register_metric("stress")
@CompositeMetric.register_metric("avgstress", scatter_reduce="mean")
class Stress(BaseLayoutMetric):

    def __init__(self, *, batch_reduce: Optional[str] = "mean", scatter_reduce: Optional[str] = "sum"):
        super().__init__(batch_reduce=batch_reduce)
        self.scatter_reduce = scatter_reduce

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        dist = torch.norm(layout.perm_dst_pos - layout.perm_src_pos, 2, 1)
        d = layout.apsp_attr
        edge_stress = dist.sub(d).abs().div(d).square()
        return torch_scatter.scatter(edge_stress, layout.perm_batch_index, reduce=self.scatter_reduce)
