from collections import deque
def bfs(n, adj_list, source):
    dist  = [float("inf") for _ in range(n)]
    dist[source] = 0
    
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        for nei in adj_list[node]:
            if dist[node]+1<dist[nei]:
                dist[nei] = dist[node]+1
                queue.append(nei)
    print(*dist, sep = ", ")

adj_list = [[1,3],[0,2,3],[1,6],[0,1,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]]

bfs(9, adj_list, 0)