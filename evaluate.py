import argparse
import json
import numpy as np
import pandas as pd

from gdbench.datasets import RomeDataset
from gdbench.nn import CompositeMetric
from gdbench.data import GraphDrawingData
from gdbench import LayoutEvaluator


def main(layout_json, output, metrics):
    layout = json.load(open(layout_json))
    GraphDrawingData.set_optional_fields(["edge_pair_metaindex", "face", "rng_index"])
    dataset = RomeDataset()
    metric = CompositeMetric(
        criteria_weights=dict(stress=1., xing=1., xangle=1., iangle=1., ring=1.),
        batch_reduce=None
    )
    evaluator = LayoutEvaluator(dataset=dataset, metrics=dict(metric=metric))
    eval_df = evaluator.evaluate(layout_dict=layout).drop('metric', axis=1)
    eval_df.to_csv(output, index=True, header=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph Drawing Benchmark")
    parser.add_argument("--layout-json", type=str, required=True,
                        help="Path to the layout TSV file")
    parser.add_argument("--output", type=str, default="metrics.csv",
                        help="Path to the output CSV file")
    parser.add_argument("--metrics", type=lambda x: x.split(","), default=["stress"],
                        help="Metrics to compute")
    args = parser.parse_args()

    main(**vars(args))
