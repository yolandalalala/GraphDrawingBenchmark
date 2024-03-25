from gdbench.data.graph_struct import GraphStruct
from .base_transformation import BaseTransformation

import torch_scatter


class Center(BaseTransformation):

    def __init__(self):
        super().__init__()

    def forward(self, layout: GraphStruct) -> GraphStruct:
        center = torch_scatter.scatter(layout.pos, layout.batch, dim=0, reduce='mean')
        return layout(layout.pos - center[layout.batch])
