def solveNQueens(n: int) -> list[list[str]]:
    def dfs(col, board, leftRow, lowDiag, uprDiag, ans):
        if col == n:
            ans.append(board)
            
        for row in range(n):
            if leftRow[row] == 0 and uprDiag[n-1+col-row] == 0 and lowDiag[col+row] == 0:
                leftRow[row] = 1
                lowDiag[col+row] = 1
                uprDiag[n-1+col-row] = 1
                
                board[row] = board[row][:col] + ["Q"] + board[row][col+1:]
                
                dfs(col+1,list(board), leftRow, lowDiag, uprDiag, ans)
                
                board[row] = board[row][:col] + ["."] + board[row][col+1:]
                
                leftRow[row] = 0
                lowDiag[col+row] = 0
                uprDiag[n-1+col-row] = 0
    
    board = [["."]*n for _ in range(n)]
    leftRow = [0]*n
    
    lowDiag = [0]*(2*n-1)
    uprDiag = [0]*(2*n-1)
    
    ans = []
    dfs(0, board, leftRow, lowDiag, uprDiag, ans)
    return ans

print(solveNQueens(4))