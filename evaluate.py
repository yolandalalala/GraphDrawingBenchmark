import argparse
import json
import numpy as np
import pandas as pd
import bigframes.pandas as bpd

from gdbench.datasets import RomeDataset
from gdbench.nn import CompositeMetric
from gdbench.data import GraphDrawingData
from gdbench import LayoutEvaluator, SPCEvaluator


def load_baseline_layout(method, split):
    print(f'Loading baseline layout for {method} on split {split}')
    return bpd.read_gbq(f'''
        SELECT L.graph_id, L.pos, S.split
        FROM `delta-chess-269600.smartgd.layouts-rome` L
        JOIN `delta-chess-269600.smartgd.splits-rome` S
        ON L.graph_id = S.graph_id
        WHERE L.method = '{method}' AND S.method = 'default' AND S.split = '{split}'
    ''', index_col='graph_id').to_pandas().pos.map(json.loads).to_dict()


def main(layout_json: str, baselines: list[str], metrics_output: str, spc_output: str, split: str, metrics: list[str]):
    layout = json.load(open(layout_json))
    GraphDrawingData.set_optional_fields(["edge_pair_metaindex", "face", "rng_index"])
    dataset = RomeDataset()
    metric = CompositeMetric(
        criteria_weights={metric: 1. for metric in metrics},
        batch_reduce=None
    )
    evaluator = LayoutEvaluator(dataset=dataset, metrics=dict(metric=metric))
    spc_evaluator = SPCEvaluator(eps=1e-5)
    metrics_df = evaluator.evaluate(layout_dict=layout).drop('metric', axis=1)
    metrics_df.to_csv(metrics_output, index=True, header=True)
    baseline_dict = {}
    for baseline in baselines:
        baseline_layout = load_baseline_layout(baseline, split)
        baseline_df = evaluator.evaluate(layout_dict=baseline_layout).drop('metric', axis=1)
        baseline_dict[baseline] = baseline_df
    spc_df = spc_evaluator.evaluate(metrics_df, baseline_dict)
    spc_df.to_csv(spc_output, index=True, header=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph Drawing Benchmark")
    parser.add_argument("--layout-json", type=str, required=True,
                        help="Path to the layout TSV file")
    parser.add_argument("--baselines", type=lambda s: s.split(','), default=["neato"],
                        help="Comma separated baseline layout algorithms to compare against")
    parser.add_argument("--metrics-output", type=str, default="metrics.csv",
                        help="Path to the output CSV file")
    parser.add_argument("--spc-output", type=str, default="spc.csv",
                        help="Path to the output CSV file")
    parser.add_argument("--split", choices=['train', 'val', 'test'], default="test",
                        help="Dataset split to evaluate on. One of 'train', 'val', 'test'")
    parser.add_argument("--metrics", type=lambda s: s.split(","), default=["stress"],
                        help="Metrics to compute")
    args = parser.parse_args()

    main(**vars(args))
