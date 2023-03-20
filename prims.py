def prim(graph, start):
    visited = set()
    msc = 0
    mse = []

    visited.add(start)

    while len(visited) < len(graph):
        mw = float('inf')
        min_edge = None
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < mw:
                    mw = weight
                    min_edge = (u, v, weight)

        if min_edge is None:
            break

        visited.add(min_edge[1])
        mse.append(min_edge)
        msc += mw

    return mse, msc


graph = {"A": [("B", 1), ("C", 3)], "B": [("A", 1), ("C", 2)], "C": [
    ("A", 3), ("B", 2), ("D", 5), ("E", 4)], "D": [("C", 5), ("E", 6)], "E": [("C", 4), ("D", 6)]}
r = prim(graph, 'A')
print(r)
print(len(graph))
