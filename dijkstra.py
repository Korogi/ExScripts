import heapq


class Vertex:

    def __init__(self, name):
        self.distance = float('inf')
        self.name = name
        self.predecessor = None
        self.discovered = False

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.distance < other.distance


def parse_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        nodes = [Vertex(name) for name in lines[0].split(", ")]

        adj = {key: [] for key in nodes}
        weights = {}

        for edge in lines[1:]:
            (start, weight, end) = edge.split(", ")
            start_node = next((node for node in nodes if node.name == start), None)
            end_node = next((node for node in nodes if node.name == end), None)

            adj[start_node].append(end_node)
            weights[(start_node, end_node)] = int(weight)

        return nodes, adj, weights


def dijkstra(vertices, s, adjacency_list, weights):
    init(vertices, s)
    q = [v for v in vertices]
    heapq.heapify(q)
    i = 0
    while len(q) > 0:
        u = heapq.heappop(q)

        for v in adjacency_list[u]:
            if v.distance > u.distance + weights[(u, v)]:
                v.distance = u.distance + weights[(u, v)]
                v.predecessor = u
                v.discovered = True
                heapq.heapify(q)  # q.decrease_key
        print_list_entry(i, vertices, q)
        i += 1


def init(vertecies, s):
    for v in vertecies:
        v.distance = float('inf')

    s.distance = 0
    s.discovered = True


def print_list_head(nodes, col="|"):
    finished_nodes = "N'"
    space = " "
    node_row = "".join([f"{col}  {n.name}  " for n in nodes])
    print(f'Iteration {col}{space*(len(nodes)) + finished_nodes + space*(len(nodes)-1)}{node_row}')


def print_list_entry(entry_number, nodes, q, col="|", inf="inf"):
    space = " "
    node_row = "".join([f"{col} {space * 3 if node not in q else get_node_entry(node, inf)} " for node in nodes])
    finished_nodes = ",".join([node.name for node in nodes if not node in q])
    print(f'{space*(len("Iteration") // 2) + str(entry_number) + space*(len("Iteration") // 2)} {col} '
          f'{finished_nodes + space*2*(len(q)) + space}'
          f'{node_row}')


def get_node_entry(node, inf):
    return f'{node.distance},{node.predecessor}' if node.distance < float('inf') else inf


def main():
    nodes, adj, weights = parse_graph_from_file("graph")
    x = list(filter(lambda v: v.name == "x", nodes))[0]

    print_list_head(nodes)
    dijkstra(nodes, x, adj, weights)
    # print([f'{node.name}: {node.distance}' for node in nodes])


if __name__ == '__main__':
    main()
