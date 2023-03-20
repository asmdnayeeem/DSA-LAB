def kruskal(graph):
    parent = {}
    rank = {}
    mst_cost = 0
    mst_edges = []

    def make_set(vertex):
        parent[vertex] = vertex
        rank[vertex] = 0

    def find_set(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_set(parent[vertex])
        return parent[vertex]

    def union(u, v):
        ra = find_set(u)
        rb = find_set(v)
        if ra != rb:
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[ra] = rb
                if rank[ra] == rank[rb]:
                    rank[rb] += 1

    for vertex in graph:
        make_set(vertex)

    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()
    for weight, u, v in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            mst_cost += weight

    return mst_edges, mst_cost


graph = {"A": [("B", 1), ("C", 3)], "B": [("A", 1), ("C", 2)], "C": [
    ("A", 3), ("B", 2), ("D", 5), ("E", 4)], "D": [("C", 5), ("E", 6)], "E": [("C", 4), ("D", 6)]}

r = kruskal(graph)
print(r)
