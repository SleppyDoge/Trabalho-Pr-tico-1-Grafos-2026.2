import sys
import threading


class Node:
    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:
    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item
            self.current = self.current.next
            return item


class Bag:
    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1


class Graph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

    def __str__(self):
        lines = ["%d vertices, %d edges" % (self.V, self.E)]
        for v in range(self.V):
            neighbors = " ".join(str(w) for w in self.adj[v])
            lines.append("%d: %s" % (v, neighbors))
        return "\n".join(lines)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return self.adj[v].size()

    def max_degree(self):
        max_deg = 0
        for v in range(self.V):
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count // 2


def read_data():
    if len(sys.argv) < 2:
        raise FileNotFoundError(
            "É necessário um arquivo txt para leitura dos dados: 'uv run main_files.py relative_filepath.txt' "
        )

    filepath = sys.argv[1]

    data = None
    with open(filepath, "r") as arquivo:
        data = arquivo.read().split()

    return data


def parse_data(raw_data: list[str]):
    results = {
        "vertices_size": int(raw_data[0]),
        "cat_tolerance": int(raw_data[1]),
        "cat_positions": [int(y) for y in raw_data[2 : 2 + int(raw_data[0])]],
        "edges": [
            (int(z), int(y))
            for z, y in zip(
                raw_data[2 + int(raw_data[0]) :: 2],
                raw_data[2 + int(raw_data[0]) + 1 :: 2],
            )
        ],
    }
    return results


class DepthFirstSearch:
    def __init__(self, G, s, cat_tolerance, is_cat):
        # kefa
        self.cat_tolerance = cat_tolerance
        self.is_cat = is_cat
        self.consec_cats = [0 for _ in range(G.V)]
        self.leafs_reached = 0

        # basic
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [-1 for _ in range(G.V)]
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v, father=None):

        self.edge_to[v] = father
        if father is None:
            self.edge_to[v] = 0

        self.consec_cats[v] = (
            self.consec_cats[self.edge_to[v]] + 1 if self.is_cat[v] == 1 else 0
        )

        self.marked[v] = True
        self.count += 1

        if self.consec_cats[v] > self.cat_tolerance:
            return

        any_sons = False
        for w in G.adj[v]:
            if not self.marked[w]:
                any_sons = True
                self.dfs(G, w, v)
        if not any_sons:
            self.leafs_reached += 1


def output_result(result: int) -> None:
    print(result)


def main():
    # read input
    raw_data = read_data()
    parsed_data = parse_data(raw_data)

    # generate graph and relevent
    graph = Graph(parsed_data["vertices_size"])
    for v, u in parsed_data["edges"]:
        graph.add_edge(v - 1, u - 1)

    search = DepthFirstSearch(
        graph, 0, parsed_data["cat_tolerance"], parsed_data["cat_positions"]
    )

    # solving
    output_result(search.leafs_reached)


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
