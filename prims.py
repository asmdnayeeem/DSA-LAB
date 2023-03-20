def prim(graph, start):
    visited = set()
    msc = 0
    mse = []

    visited.add(start)

    while len(visited) < len(graph):
        mw = float('inf')
        me = None
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < mw:
                    mw = weight
                    me = (u, v, weight)

        if me is None:
            break

        visited.add(me[1])
        mse.append(me)
        msc += mw

    return mse, msc


graph = {"A": [("B", 1), ("C", 3)], "B": [("A", 1), ("C", 2)], "C": [
    ("A", 3), ("B", 2), ("D", 5), ("E", 4)], "D": [("C", 5), ("E", 6)], "E": [("C", 4), ("D", 6)]}
r = prim(graph, 'A')
print(r)
print(len(graph))
