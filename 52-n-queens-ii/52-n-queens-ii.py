class Solution:
    def solve(self,col,board,res,leftRow,upperDia,lowerDia,n):
        if col==n:
            res.append(["".join(r) for r in board])
            return 
        for row in range(n):
            if leftRow[row]==0 and lowerDia[row+col]==0 and upperDia[n-1+col-row]==0:
                board[row][col] = 'Q'
                leftRow[row] = 1
                upperDia[n-1+col-row] = 1
                lowerDia[row+col] = 1
                self.solve(col+1,board,res,leftRow,upperDia,lowerDia,n)
                board[row][col] = '.'
                leftRow[row] = 0
                upperDia[n-1+col-row] = 0
                lowerDia[row+col] = 0
    def totalNQueens(self, n: int) -> int:
        board = [['.']*n for i in range (n)]
        res = []
        self.solve(0,board,res,[0]*n,[0]*(2*n-1),[0]*(2*n-1),n)
        return len(res)