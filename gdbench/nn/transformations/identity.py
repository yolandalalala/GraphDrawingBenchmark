from gdbench.data.graph_struct import GraphStruct
from .base_transformation import BaseTransformation


class Identity(BaseTransformation):

    def __init__(self):
        super().__init__()

    def forward(self, layout: GraphStruct) -> GraphStruct:
        return layout
