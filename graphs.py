#representation
graph1={"A":["B","C"],"B":[],"C":["D"],"D":[]}

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

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
BFS(graph, '5')

def DFS(graph,node):
    pass

visited = set() 

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')