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
            
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range (n)]
        res = []
        self.solve(0,board,res,[0]*n,[0]*(2*n-1),[0]*(2*n-1),n)
        return res
        
#-----------------------------------Approach 2---------------------------------------------
# class Solution:
#     def isSafe(self,row,col,board,n):
#         dup_row,dup_col = row,col
#         while(row>=0 and col>=0):     #check upper diagonal
#             if(board[row][col]=='Q'):
#                 return False
#             col -= 1
#             row -= 1
#         col,row = dup_col,dup_row
#         while(col>=0):     #chcek horizontally to the Left
#             if(board[row][col]=='Q'):
#                 return False
#             col -= 1
#         row,col = dup_row,dup_col
#         while(row<n and col>=0):       #check lower diagonal
#             if(board[row][col]=='Q'):
#                 return False
#             row += 1
#             col -= 1
#         return True
    
#     def solve(self,col,board,res,n):
#         if col == n:
#             res.append(["".join(r) for r in board])
#             return
#         for row in range(n):
#             if(self.isSafe(row,col,board,n)):
#                 board[row][col]='Q'
#                 self.solve(col+1,board,res,n)
#                 board[row][col]='.'
    
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         board = [['.']*n for i in range (n)]
#         res = []
#         self.solve(0,board,res,n)
#         return res