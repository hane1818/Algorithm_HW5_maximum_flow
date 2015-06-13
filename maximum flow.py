import sys

"""
class Edge(object):
    def __init__(self, src, dest, flow):
        self.src = src
        self.dest = dest
        self.max_flow = flow
"""


def breadth_first_search(graph, source, sink):
    queue = [source]
    path = {source: []}

    while queue:
        src = queue.pop(0)
        for dest in range(len(graph)):
            if graph[src][dest] > 0 and dest not in path:
                path[dest] = path[src] + {(src, dest)}
                if dest == sink:
                    return path[dest]
                queue.append(dest)

    return None


def edmonds_karp(graph, source, sink):
    max_flow = 0

    while True:
        path = breadth_first_search(graph, source, sink)
        if not path:
            break
        flow = min(graph[i][j] for i, j in path)
        for i, j in path:
            graph[i][j] -= flow
            graph[j][i] += flow
        max_flow += flow

    return max_flow


def main():
    line = input().split(" ")
    V = int(line[0])
    E = int(line[1])

    line = input().split(" ")
    source = int(line[0])
    sink = int(line[1])

    graph = [[0 for i in range(V+1)] for j in range(V+1)]
    for i in range(E):
        line = input().split(" ")
        graph[int(line[1])][int(line[2])] = int(line[0])


if __name__ == '__main__':
    main()
    sys.exit()
