#Topological Sorting is only possible in Directed Acyclic Graphs
#DFS
def topoSort(V, adj):
    visited = [0 for i in range(V)]
    ds = []
    
    def dfs(node):
        visited[node] = 1
        
        for neigh in adj[node]:
            if visited[neigh] == 0:
                dfs(neigh)
        
        ds.append(node)
        
    for i in range(V):
        if visited[i] == 0:
            dfs(i)
    
    return ds[::-1] #better use deque and append left

#BFS:
from collections import deque
def bfs( n, adj_list):
    in_degree = [0 for i in range(n)]
    for i in range(n):
        for x in adj_list[i]:
            in_degree[x] += 1
    
    queue = deque()
    res = []
    
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    cnt = 0
    while queue:
        node = queue.pop()
        cnt+=1
        res.append(node)
        for nei in adj_list[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
            
    if cnt == n:
        return res #no cycle
    return [] #cycle topo sort not possible