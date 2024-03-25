from gdbench.constants import EPS
from gdbench.data import GraphStruct
from gdbench.nn.ops import EdgesIntersect
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch.nn.functional as F
import torch_scatter


@CompositeMetric.register_metric("xangle")
@CompositeMetric.register_metric("avgxangle", scatter_reduce="mean")
class CrossingAngleCritic(BaseLayoutMetric):

    def __init__(self, *,
                 eps: float = EPS,
                 scatter_reduce: Optional[str] = "sum",
                 batch_reduce: Optional[str] = "mean"):
        super().__init__(batch_reduce=batch_reduce)
        self.scatter_reduce = scatter_reduce
        self.intersect = EdgesIntersect(eps=eps)

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        (s1, s2), (e1, e2) = layout.edge_pair_index

        xing = self.intersect(
            edge_1_start_pos=layout.pos[s1],
            edge_1_end_pos=layout.pos[e1],
            edge_2_start_pos=layout.pos[s2],
            edge_2_end_pos=layout.pos[e2]
        )

        r, s = layout.pos[e1] - layout.pos[s1], layout.pos[e2] - layout.pos[s2]
        radians = (F.normalize(r, dim=1) * F.normalize(s, dim=1)).sum(dim=1).abs().asin()
        radians[~xing] = 0

        if self.scatter_reduce is None:
            return radians

        return torch_scatter.scatter(radians, layout.batch[s1],
                                     reduce=self.scatter_reduce,
                                     dim_size=layout.num_graphs)
