class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bellman_kalaba(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u in range(self.V):
                for v in range(self.V):
                    if self.graph[u][v] != 0 and dist[u] != float('inf') and dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]

        return dist[self.V - 1]

def main():
    g = Graph(5)
    g.add_edge(0, 1, 2)  # A -> B
    g.add_edge(1, 2, 3)  # B -> C
    g.add_edge(0, 2, 5)  # A -> C
    g.add_edge(0, 3, 2)  # A -> D
    g.add_edge(3, 4, 7)  # D -> E
    g.add_edge(4, 2, 1)  # E -> C

    longest_distance = g.bellman_kalaba(0)

    print("Le chemin le plus long est A -> C avec une distance de", longest_distance)

if __name__ == "__main__":
    main()
