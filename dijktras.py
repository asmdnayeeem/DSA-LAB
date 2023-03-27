import math
inf = math.inf
def dijktras(graph, node):
    d = {}
    for i in graph:
        d[i] = inf
    d[node] = 0
    for i in graph:
        for j, k in graph[i]:
            if d[j] > d[i]+k:
                d[j] = d[i]+k
    for i in d:
        print(node,"-->",i,':',d[i])
    return d
    
graph = {"A": [("B", 1), ("C", 3)], "B": [("A", 1), ("C", 2)], "C": [
    ("A", 3), ("B", 2), ("D", 5), ("E", 4)], "D": [("C", 5), ("E", 6)], "E": [("C", 4), ("D", 6)]}
graph1 = {"A": [("B", 2), ("C", 3), ("D", 8)],
          "B": [("A", 2), ("D", 4)],
          "C": [("A", 3), ("D", 6), ("E", 9)],
          "D": [("A", 8), ("B", 4), ("C", 6), ("F", 4)],
          "E": [("C", 9), ("F", 3)],
          "F": [("D", 4), ("E", 3)]}
dijktras(graph, 'A')
dijktras(graph1, 'A')
