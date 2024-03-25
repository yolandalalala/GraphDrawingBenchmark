from gdbench.data import GraphStruct
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch_scatter


@CompositeMetric.register_metric("absedge", abs_edge_len=1.)
@CompositeMetric.register_metric("edge")
class EdgeVar(BaseLayoutMetric):

    def __init__(self, *,
                 abs_edge_len: Optional[float] = None,
                 batch_reduce: Optional[str] = "mean"):
        super().__init__(batch_reduce=batch_reduce)
        self.abs_edge_len: Optional[float] = abs_edge_len

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        dist = layout.edge_dst_pos.sub(layout.edge_src_pos).norm(dim=1)
        edge_var = dist.sub(self.abs_edge_len or dist.mean()).square()
        return torch_scatter.scatter(edge_var, layout.edge_batch_index, reduce="mean")
