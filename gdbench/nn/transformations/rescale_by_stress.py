from gdbench.data.graph_struct import GraphStruct
from .base_transformation import BaseTransformation

import torch_scatter


class RescaleByStress(BaseTransformation):

    def __init__(self):
        super().__init__()

    def forward(self, layout: GraphStruct) -> GraphStruct:
        dist = (layout.perm_dst_pos - layout.perm_src_pos).norm(dim=1)
        u_over_d = dist / layout.apsp_attr
        scatterd_u_over_d_2 = torch_scatter.scatter(u_over_d ** 2, layout.perm_batch_index)
        scatterd_u_over_d = torch_scatter.scatter(u_over_d, layout.perm_batch_index)
        scale = scatterd_u_over_d_2 / scatterd_u_over_d
        return layout(layout.pos / scale[layout.batch][:, None])
