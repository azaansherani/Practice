import collections

# #BFS
def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    
    rows, cols = len(grid), len(grid[0])
    
    visited = set()
    
    def bfs(x, y):
        queue = collections.deque()
        queue.append((x, y))
        visited.add((x,y))
        
        directions = [(0,1), (1,0), (0, -1), (-1, 0), (1,1), (-1,-1), (-1,1), (1,-1)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                r, c = x+dx, y+dy
                
                if (r>=0 and r<rows and c in range(0, cols) and
                    (r, c) not in visited and grid[r][c] == "1"):
                        queue.append((r,c))
                        visited.add((r,c))
                    
            
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if (i,j) not in visited and grid[i][j] == "1":
                islands += 1
                bfs(i, j)
    
    return islands

grid = [["1","1","0","0","1"],
        ["1","1","0","1","0"],
        ["0","0","1","0","0"],
        ["0","1","0","1","1"]]

print(numIslands(grid))

#DFS
def numIslands(grid) -> int:

    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def dfs(i,j):
        if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!="1" or ((i,j) in visited):
            return
        
        visited.add((i,j))
        dfs(i,j+1)
        dfs(i, j-1)
        dfs(i+1,j)
        dfs(i-1,j-1)
        dfs(i-1,j+1)
        dfs(i+1,j-1)
        dfs(i+1,j+1)
    
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if (i,j) not in visited and grid[i][j] == "1":
                islands += 1
                dfs(i,j)
                
    
    return islands