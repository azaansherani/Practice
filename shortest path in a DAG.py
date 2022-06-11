def shortestPath(n, adj_list, source):
    topoStack = []
    visited = [0 for i in range(n)]

    def topoSort(node):
        visited[node] = 1

        for nei, edgeWeight in adj_list[node]:
            if visited[nei] == 0:
                topoSort(nei)
            
        topoStack.append(node)

    for i in range(n):
        if visited[i] == 0:
            topoSort(i)
    
    print(topoStack)
    dist = [float("inf")]*n
    dist[source] = 0

    while topoStack:
        node = topoStack.pop()    #dfs se topo stack ulta aata h 
        if dist[node] != float("inf"):   #making sure source se start ho, or source se accessible neighbors ka hi distance nikaalega
            for neighbor, edgeWeight in adj_list[node]:
                if dist[node] + edgeWeight < dist[neighbor]:
                    dist[neighbor] = dist[node] + edgeWeight
    
    print("dist array: ", *dist, sep = ' ')

adj_list = [
            [(1,2),(4,1)],
            [(2,3)],
            [(3,6)],
            [],
            [(2,2), (5,4)],
            [(3,1)]
            ]

shortestPath(6,adj_list, 0)

"""
adj_list: at index = node: (neighbor node, weight of edge from node to neighbor) 
"""