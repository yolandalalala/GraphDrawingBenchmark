from gdbench.data import GraphStruct
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch_scatter


# TODO: scale invariance
@CompositeMetric.register_metric("tsne")
@CompositeMetric.register_metric("avgtsne", scatter_reduce="mean")
class TSNEScore(BaseLayoutMetric):

    def __init__(self, *,
                 sigma: float = 1.,
                 batch_reduce: Optional[str] = "mean",
                 scatter_reduce: Optional[str] = "sum"):
        super().__init__(batch_reduce=batch_reduce)
        self.sigma: float = sigma
        self.scatter_reduce = scatter_reduce

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        p = layout.apsp_attr.div(-2 * self.sigma ** 2).exp()
        sum_src = torch_scatter.scatter(p, layout.perm_src_index)[layout.perm_src_index]
        sum_dst = torch_scatter.scatter(p, layout.perm_dst_index)[layout.perm_dst_index]
        p = (p / sum_src + p / sum_dst) / (2 * layout.n[layout.perm_batch_index])
        dist = layout.perm_dst_pos.sub(layout.perm_src_pos).norm(dim=1)
        index = layout.perm_batch_index
        q = 1 / (1 + dist.square())
        q /= torch_scatter.scatter(q, index)[index]
        edge_kl = (p.log() - q.log()).mul(p)
        return torch_scatter.scatter(edge_kl, index, reduce=self.scatter_reduce)
