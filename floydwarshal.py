import math
inf=math.inf
def fwa(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k]+graph[k][j]<graph[i][j]:
                    graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    return graph

graph=[[0,1,3,inf,inf],[1,0,2,inf,inf],[3,2,0,5,4],[inf,inf,5,0,6],[inf,inf,4,6,0]]
print(fwa(graph,5))