from ..batch_operation import BatchOperation

import torch
from torch import nn
import torch_sparse
import torch_scatter


class JaccardIndex(BatchOperation):

    def compute(self,
                edge_index_1: torch.LongTensor,
                edge_index_2: torch.LongTensor,
                *,
                batch_index: torch.LongTensor) -> torch.Tensor:
        cat_index = torch.cat([edge_index_1, edge_index_2], dim=1)
        merged_index, merged_value = torch_sparse.coalesce(
            index=cat_index,
            value=torch.ones_like(cat_index[0]),
            m=len(batch_index),
            n=len(batch_index)
        )
        intersection = torch_scatter.scatter((merged_value > 1).to(float), merged_index[0])
        union = torch_scatter.scatter((merged_value > 0).to(float), merged_index[0])
        return torch_scatter.scatter(intersection / union, batch_index, reduce="mean")
