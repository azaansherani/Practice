from collections import deque

# undirected , acyclic, unweighted, adj is Adjacency lit, V is vertices
def dfsOfGraph(V, adj):    
    def dfs(node, adj, vis, res):
        res.append(node)
        vis[node] = 1
        for nei in adj[node]:
            if vis[nei]==0:
                dfs(nei, adj, vis, res)
        
    vis = [0 for i in range(V)]
    res = []
    for i in range(0,V): #0 indexed graph
        if vis[i] == 0:
            dfs(i, adj, vis, res)
    
    return res

# directed, adj is Adjacency list, V is vertices
def bfsOfGraph( V, adj):
    vis = [0 for i in range(V)]
    res = []
    queue = deque()
    queue.append(0)
    vis[0] == 1
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbour in adj[node]:
            if vis[neighbour] == 0:
                queue.append(neighbour)
                vis[neighbour] = 1
    return res


# undirected , edges is a list having two lists such that list[0][i] and list[1][i] has an edge between them
def BFS(V, edges):
    adj = [[] for i in range(V)]
    for i,j in zip(edges[0], edges[1]):
        adj[i].append(j)
        adj[j].append(i)

    for i in adj: i.sort()
    vis = [0 for i in range(V)]
    res = []
    queue = deque()
    for i in range(V):
        if vis[i] == 0:
            queue.append(i)
            vis[i] = 1
            while queue:
                node = queue.popleft()
                res.append(node)
                for adjNode in adj[node]:
                    if vis[adjNode] == 0:
                        queue.append(adjNode)
                        vis[adjNode] = 1
    return res

#another way to do the above bfs problem by making an adjacency matrix
def BFS(V, edges):
	adjmatrix = [[0 for i in range(V)] for j in range(V)]
	vis = [0 for i in range(V)]
	res = []
	for i in range(len(edges[0])):
		adjmatrix[edges[0][i]][edges[1][i]] = 1
		adjmatrix[edges[1][i]][edges[0][i]] = 1
	q = deque()
	for i in range(V):
		if vis[i] == 0:
			q.append(i)
			vis[i] = 1
			while q:
				node = q.popleft()
				res.append(node)
				for i in range(len(adjmatrix)):
					if adjmatrix[node][i] == 1 and vis[i] == 0:
						q.append(i)
						vis[i] = 1
	return res