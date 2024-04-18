# Write a program that implements a breadth-first search (BFS) in a graph represented by adjacency lists.
class Root:
    def __init__(self, key):
        self.key = key
        self.children = []



def bfs(root: Root):
    queue = [root]
    while queue:
        print(queue[0].key, end=" ")
        node = queue.pop(0)

        if node.children:
            queue.extend(node.children)

