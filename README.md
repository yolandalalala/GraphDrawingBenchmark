# Graph Drawing Benchmark

## Input format
Input file is a JSON file with the following format:
```
{
  "<graph1_id>": [
    [<node1_x>, <node1_y>],
    [<node2_x>, <node2_y>],
    ...
  ],
  "<graph_id_2>": [
    [<node1_x>, <node1_y>],
    [<node2_x>, <node2_y>],
    ...
  ],
  ...
}
```
See `example_layouts.json` for an example.

## Evaluation
```sh
python main.py eval \
--layout-json example_layouts.json \
--baselines neato,kamada_kawai \
--metrics-output metrics.csv \
--spc-output spc.csv \
--metrics stress,xing,ring \
--split test
```
* --layout-json: Path to the input JSON file.
* --baselines: Comma-separated list of baseline layout algorithms.
* --metrics-output: Path to the output CSV file for evaluation metrics.
* --spc-output: Path to the output CSV file for metrics SPCs.
* --metrics: Comma-separated list of evaluation metrics.
* --split: Dataset split to evaluate. (train, val, test)

## Print graph IDs for a specific dataset split
```sh
python main.py info splits --name <split>
```

## Print available baseline layout algorithms
```sh
python main.py info baselines
```

## Print available evaluation metrics
```sh
python main.py info metrics
```
