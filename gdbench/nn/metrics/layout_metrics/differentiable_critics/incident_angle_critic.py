from gdbench.data import GraphStruct
from gdbench.nn.ops import SparseSort
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch
import torch.nn.functional as F
import numpy as np
import torch_scatter


@CompositeMetric.register_metric("iangle")
@CompositeMetric.register_metric("avgiangle", scatter_reduce="mean")
class IncidentAngle(BaseLayoutMetric):

    def __init__(self, *, batch_reduce: Optional[str] = "mean", scatter_reduce: Optional[str] = "sum"):
        super().__init__(batch_reduce=batch_reduce)
        self.sparse_sort = SparseSort()
        self.scatter_reduce = scatter_reduce

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        angles = self.get_counter_clockwise_sorted_angles(pos=layout.pos, adj_index=layout.edge_index)
        u, v1, v2 = angles[0], angles[1], angles[2]
        e1 = F.normalize(layout.pos[v1] - layout.pos[u])
        e2 = F.normalize(layout.pos[v2] - layout.pos[u])
        theta = (e1 * e2).sum(dim=1).clamp(min=-1, max=1).acos()
        src = layout.edge_src_index
        degrees = torch_scatter.scatter(torch.ones_like(src), src, dim_size=len(layout.pos))[u]
        phi = degrees.float().pow(-1).mul(2*np.pi)
        angle_l1 = phi.sub(theta).abs()
        return torch_scatter.scatter(angle_l1, layout.batch[u], reduce=self.scatter_reduce)

    def get_counter_clockwise_sorted_angles(self, *,
                                            pos: torch.FloatTensor,
                                            adj_index: torch.LongTensor) -> torch.Tensor:
        u, v = adj_index
        diff = F.normalize(pos[v] - pos[u])
        # get cosine angle between uv and x-axis
        cos, sin = diff.T
        # get radian between uv and x-axis
        radian = cos.acos() * sin.sign()
        # for each u, sort edges based on the position of v
        perm = self.sparse_sort(radian, u)[-1]
        sorted_v = v[perm]
        counts = torch.unique(u, return_counts=True)[-1]
        # get start index for each u
        last_idx = counts.cumsum(0) - 1
        roll_val = torch.arange(len(u)).to(last_idx)
        roll_val[last_idx] -= len(u)
        roll_perm = self.sparse_sort(roll_val, u)[-1]
        rolled_v = sorted_v[roll_perm]
        return torch.stack([u, sorted_v, rolled_v]).T[sorted_v != rolled_v].T
