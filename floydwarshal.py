import math
inf=math.inf
def fwa(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k]+graph[k][j]<graph[i][j]:
                    graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    return graph

# n=int(input("Enter the number of nodes: "))
# graphs=[]
# for i in range(n):
#     graphs.append(list(map(int,input().split())))

graph=[[0,1,3,inf,inf],[1,0,2,inf,inf],[3,2,0,5,4],[inf,inf,5,0,6],[inf,inf,4,6,0]]
print(fwa(graph,5))
# graph1=[[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]]
# print(fwa(graph1,4))