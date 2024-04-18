# Write a program that implements a aplgorithm to find the shortest path in a weighted graph using a Dijkstra algorithm.
class Dijsktra:

    def __init__(self, vertexs: int):
        self.vertexs = vertexs
        self.graph = []

    def add_edge(self, origin: int, destination: int, weight: int):
        self.graph.append([origin, destination, weight])

    def start(self, source: int):
        dist = [float("inf")] * self.vertexs
        dist[source] = 0

        for o, d, w in self.graph:
            min_weight = dist[o] + w
            if dist[d] == float("inf"):
                destinations = list(filter(lambda x: x[1] == d, self.graph))
                if len(destinations) > 1:
                    min_weight = min([x[2] for x in destinations])
                    shortest_path = list(filter(lambda x: x[2] == min_weight, destinations))
                    min_weight = shortest_path[0][2] + dist[shortest_path[0][0]]

                dist[d] = min_weight

        print("Vertex Distance from Source")
        for i in range(self.vertexs):
            print(f"{i}\t{dist[i]}")
    
