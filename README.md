# Algorithm_HW5_maximum_flow
Learn how to implement Edmonds-Karp algorithm to find maximum flow from source to sink

## How to use
```bash
$ python "maximum flow.py"
```
## Input type
```py
6 7
1 6
5 1 2
2 2 5
6 1 3
4 2 4
4 5 6
7 3 4
8 4 6
# First line contains two integer V, E, indicating the number of nodes and edges.
# Second line contains the vertex index of source and sink.
# In the following E lines, each contains w, v1 & v2, indicating an edge with weight between v1 & v2.
```
## Output type
```py
10
# The maximum flow from source to sink.
```
