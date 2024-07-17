def bellman_kalaba(graph, source): 
    num_vertices = len(graph) 
    distances = [float('-inf')] * num_vertices 
    distances[source] = 0 
 
    for _ in range(num_vertices - 1): 
        for u in range(num_vertices): 
            for v, weight in graph[u]: 
                if distances[u] + weight > distances[v]: 
                    distances[v] = distances[u] + weight 
 
    for u in range(num_vertices): 
        for v, weight in graph[u]: 
            if distances[u] + weight > distances[v]: 
                print("Le graphe contient un cycle absorbant.") 
                return 
 
    print("Distances depuis le sommet source", source) 
    for i in range(num_vertices): 
        print("Sommet", i, ": Distance =", distances[i]) 
 
# Exemple de graphe 
graph = [ 
    [(1, -1), (2, 4)], 
    [(2, 3), (3, 2), (4, 2)], 
    [(3, 5)], 
    [(1, 1), (2, -3)], 
    [] 
] 
 
source = 0 
bellman_kalaba(graph, source)

