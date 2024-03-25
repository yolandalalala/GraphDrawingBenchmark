from gdbench.data import GraphStruct
from ..base_layout_metric import BaseLayoutMetric
from ..composite_metric import CompositeMetric

from typing import Optional

import torch


@CompositeMetric.register_metric("sss")
class SimpleShapeScore(BaseLayoutMetric):

    def __init__(self, *, batch_reduce: Optional[str] = "mean"):
        super().__init__(batch_reduce=batch_reduce)

    def compute(self, layout: GraphStruct) -> torch.Tensor:
        shape_score = []
        for l in layout.split():
            raw_edges = l.edge_adj.idx.T.cpu().numpy()
            sss = simple_shape_score(l.pos.detach().cpu().numpy(), raw_edges, k=self.k)
            shape_score.append(torch.tensor(sss).to(l.pos))
        return torch.stack(shape_score)

    # TODO: torchfy
    # TODO: fix logic
    def simple_shape_score(pos, edge_set, k=3):
        G = nx.Graph(edge_set.tolist())
        apsp = dict(nx.all_pairs_shortest_path_length(G))
        full_edges, attr_d = zip(*[((u, v), d) for u in apsp for v, d in apsp[u].items() if u != v])
        full_index, d = np.array(full_edges).T, np.array(attr_d)
        src, dst = pos[full_index[0]], pos[full_index[1]]
        u = np.linalg.norm(dst - src, axis=1)
        d_mat = sparse.coo_matrix((d, full_index)).toarray()  # TODO: specify shape
        u_mat = sparse.coo_matrix((u, full_index)).toarray()
        kth_dist = u_mat[np.indices(d_mat.shape)[0], d_mat.argsort(axis=1)][:, :k+1].max(axis=1)
        return np.mean(k / (np.sum(u_mat <= kth_dist[:, None], axis=1) - 1))
