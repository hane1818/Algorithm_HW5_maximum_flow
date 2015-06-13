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


def main():
    pass

if __name__ == '__main__':
    main()
    sys.exit()
