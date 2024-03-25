from gdbench.data import GraphStruct
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch_scatter


@CompositeMetric.register_metric("ring")
@CompositeMetric.register_metric("avgring", scatter_reduce="mean")
class Occlusion(BaseLayoutMetric):

    def __init__(self, *, gamma: float = 1., batch_reduce: Optional[str] = "mean", scatter_reduce: Optional[str] = "sum"):
        super().__init__(batch_reduce=batch_reduce)
        self.gamma: float = gamma
        self.scatter_reduce = scatter_reduce

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        dist = layout.perm_dst_pos.sub(layout.perm_src_pos).norm(dim=1)
        edge_occlusion = dist.mul(-self.gamma).exp()
        return torch_scatter.scatter(edge_occlusion, layout.perm_batch_index, reduce=self.scatter_reduce)
