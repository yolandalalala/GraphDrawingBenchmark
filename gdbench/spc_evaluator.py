import numpy as np
import pandas as pd


class SPCEvaluator:

    def __init__(self, eps: float):
        self.eps = eps

    def evaluate(self, metrics, baseline_dict):
        spc_series_list = []
        for name, baseline in baseline_dict.items():
            spc_series = ((metrics - baseline) / np.maximum(metrics + self.eps, baseline + self.eps)).mean()
            spc_series.name = name
            spc_series_list.append(spc_series)
        return pd.DataFrame(spc_series_list)
