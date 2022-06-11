from collections import deque

#BFS Solution O(mn)
def walls_and_gates(self, rooms: list[list[int]]):
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                queue.append((i,j))

    while queue:
        size = len(queue)
        for i in range(size):
            row, col = queue.popleft()

            for dr, dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                r = row + dr
                c = col + dc
                if 0<=r<rows and 0<=c<cols and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r,c))

# DFS, Time Limit Exceeded as worst case is O(mn^2)
def walls_and_gates(rooms: list[list[int]]):
    rows, cols = len(rooms), len(rooms[0])
    visited = set()
    def dfs(r, c, dist = 0):
        if r<0 or r>=rows or c<0 or c>=cols or rooms[r][c] == -1 or (r,c) in visited:
            return
        visited.add((r,c))
        rooms[r][c] = min(rooms[r][c], dist)
        dfs(r,c+1, dist+1)
        dfs(r,c-1,dist+1)
        dfs(r-1,c, dist+1)
        dfs(r+1,c, dist + 1)
        visited.discard((r,c))
                
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                dfs(i, j)