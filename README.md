# Graph Drawing Benchmark

## Input Format
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
python evaluate.py \
--layout-json example_layouts.json \
--baselines neato,kamada_kawai \
--metrics-output metrics.csv \
--spc-output spc.csv \
--metrics stress,xing,ring \
--split test
```