
# Write a program that implement a algorithm to find the shortest path in a weighted graph using a Bellman-Ford algorithm.
class BellmanFord:

    def __init__(self, vertexs: int):
        self.vertexs = vertexs
        self.graph = []


    def add_edge(self, origin: int, destination: int, weight: int):
        self.graph.append([origin, destination, weight])

    
    def start(self, source: int):
        dist = [float("inf")] * self.vertexs
        dist[source] = 0

        for _ in range(self.vertexs - 1):
            for o, d, w in self.graph:
                shortest_path = (dist[o] + w)
                if dist[o] != float("inf") and dist[d] > shortest_path:
                    dist[d] = shortest_path
        
        for o, d, w in self.graph:
            if dist[d] > (dist[o] + w):
                print("Graph contains negative weight cycle")
                return

        print("Vertex Distance from Source")
        for i in range(self.vertexs):
            print(f"{i}\t{dist[i]}")
