# Bellman-Ford Algorithm

def bellman_ford(edges, V, source):
    # Step 1: Initialize distances
    dist = [float('inf')] * V
    dist[source] = 0

    # Step 2: Relax all edges (V-1 times)
    for i in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative weight cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Negative weight cycle detected")
            return

    # Print result
    print("Vertex Distance from Source")
    for i in range(V):
        print(i, "->", dist[i])


# Main program
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))

bellman_ford(edges, V, source)