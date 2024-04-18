

"""
Write a program that implements a depth-first search (DFS) in a graph represented by adjacency lists.
"""
class Graph:

    def __init__(self):
        self.graph = {}
        self.visited = set()


    def add_edge(self, u: list, v: int):
        self.graph.setdefault(u, []).append(v)


    def dfs(self, node: int):
        self.visited.add(node)
        print(node, end=" ")

        for n in self.graph.get(node, []):
            if n not in self.visited:
                self.dfs(n)
