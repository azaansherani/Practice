# DFS Undirected
def detectCycle(i, parent, visited, adj):
    visited[i] = 1
    
    for nei in adj[i]:
        if visited[nei] == 0:
            if detectCycle(nei, i, visited, adj): return True
        
        elif nei != parent:
            return True
    
    return False

def isCycle( V, adj):
    visited = [0 for i in range(V)]
    for i in range(V):
        if visited[i] == 0:
            if detectCycle(i, -1, visited, adj): return True
    
    return False

from collections import deque, defaultdict
#bfs undirected
def isCycle(V, adj):
    queue = deque()
    visited = [0 for i in range(V)]
    
    for i in range(V):
        if visited[i] == 0:
            queue.append((i, -1))
            visited[i] = 1
            while queue:
                node, parent = queue.popleft()
                for nei in adj[node]:
                    if visited[nei] == 0:
                        queue.append((nei, node))
                        visited[nei] = 1
                    elif nei!=parent:
                        return True
    return False

#dfs directed, 1 indexed graph, solution 1

def solve(self, A, B):
    adj_list = defaultdict(list)
    visited = [0 for i in range(A+1)]
    dfs = [0 for i in range(A+1)] #basically jo jo node parent h tick krdo

    for i in range(len(B)):
        adj_list[B[i][0]].append(B[i][1])  # B was like [[1,2], [2,3], [3,2]]

    for i in range(1, A+1):
        if visited[i] == 0:
            if checkCycle(i, dfs, visited, adj_list): return 1

    return 0

    
def checkCycle(node, dfs, visited, adj_list):
    visited[node] = 1
    dfs[node] = 1

    for child in adj_list[node]:
        if visited[child] == 0:
            if checkCycle(child, dfs, visited, adj_list): return 1
        
        elif dfs[child] == 1: return 1

    dfs[node] = 0

    return 0

#solution 2
def solve(A, B):
    adj_list = defaultdict(list)
    visited = [0 for i in range(A)]
    parent = set()
    for i in range(len(B)):
        adj_list[B[i][0]].append(B[i][1])

    for i in range(0,A):
        if visited[i]==0:
            if checkCycle(i, parent, visited, adj_list): return 1
    
    return 0
    
def checkCycle(node, parent, visited, adj_list):
    visited[node] = 1
    parent.add(node)
    for child in adj_list[node]:
        if visited[child] == 0:
            if checkCycle(child, parent, visited, adj_list): return 1
        
        elif child in parent: return 1  
    parent.discard(node)
    #for topological sort append node into result array here
    return 0


#BFS DIRECTED and Topological Sort:
def solve( n, adj_list):
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