def numProvinces(adjMatrix, V):
    visited = [0 for i in range(V)]
    
    
    def dfs(node):
        visited[node] = 1
        
        for i in range(V):
            if adjMatrix[node][i] == 1 and visited[i] == 0:
                dfs(i)
    
    provinces = 0
    for i in range(V):
        if visited[i] == 0:
            provinces += 1
            dfs(i)
    
    return provinces