#representation
graph1={"A":["B","C"],"B":["C","D"],"C":["E","F"],"D":[],"E":["G"],"F":["G"],"G":[]}

#BFS
def BFS(graph, node): 
  visited=[]  
  queue=[]
  visited.append(node)
  queue.append(node)

  while queue:        
    m = queue.pop(0) 
    print (m, end = " ") 

    for next in graph[m]:
      if next not in visited:
        visited.append(next)
        queue.append(next)
  print()  

print("Following is the Breadth-First Search")
BFS(graph1, 'A')
#DFS
visited1 = []
def dfs(visited1, graph, node): 
    if node not in visited1:
        print (node,end=" ")
        visited1.append(node)
        for next in graph[node]:
            dfs(visited1, graph, next)


print("Following is the Depth-First Search")
dfs(visited1, graph1, 'A')
print()


