import pandas as pd

from .nn import (
    CompositeMetric,
    BaseLayoutMetric,
    BaseTransformation,
    Compose,
    Center,
    NormalizeRotation,
    RescaleByStress
)

import numpy as np
from torch_geometric.data import Dataset, Batch


class LayoutEvaluator:

    dataset: Dataset
    metrics: dict[str, CompositeMetric]
    canonicalize: BaseTransformation

    def __init__(self, dataset: Dataset, metrics: dict[str, CompositeMetric]):
        self.dataset = dataset
        self.metrics = metrics
        for name, metric in metrics.items():
            assert metric.reduce.reduce == "none", f"batch_reduce for '{name}' is not None!"
        self.canonicalize = Compose(
            Center(),
            NormalizeRotation(),
            RescaleByStress()
        )

    def _is_valid_layout(self, name_pos):
        name, pos = name_pos
        return not np.isnan(pos).any()

    def evaluate(self, layout_dict: dict[str, np.ndarray]):
        layout_dict = dict(filter(self._is_valid_layout, layout_dict.items()))
        data_list = list(filter(lambda data: data.name in layout_dict, self.dataset))
        batch = Batch.from_data_list(data_list)
        x = batch.make_struct(layout_dict)
        x = batch.transform_struct(transform=self.canonicalize, struct=x)
        evaluations = {}
        for name, metric in self.metrics.items():
            evaluations[name] = metric(x).detach().cpu().numpy()
            evaluations.update({k: v.detach().cpu().numpy() for k, v in metric.get_raw_scores().items()})
        df = pd.DataFrame(evaluations, index=batch.name)
        name_list = [data.name for data in self.dataset]
        for name in name_list:
            if name not in layout_dict:
                df.loc[name, :] = None
        result_df = df.loc[name_list]
        result_df.index.name = "graph_id"
        return result_df
