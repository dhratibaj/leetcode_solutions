class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalidnbr(r,c):
            if r>=0 and r<len(board) and c>=0 and c<len(board[0]):
                return True
            return False
        
        dx = [0,0,1,1,1,-1,-1,-1]
        dy = [1,-1,1,-1,0,0,1,-1]
        for row in range(len(board)):
            for col in range(len(board[0])):
                livenbr = 0
                for i in range(8):
                    checkrow = row+dx[i]
                    checkcol = col+dy[i]
                    if isvalidnbr(checkrow, checkcol) and abs(board[checkrow][checkcol]) == 1:
                        livenbr+=1
                        # if row == 1 and col == 0:
                        # # print(board, abs(board[row][col]))
                        #     print(checkrow, checkcol, livenbr)
                if board[row][col] == 1 and (livenbr<2 or livenbr>3):
                    board[row][col] = -1
                if board[row][col] == 0 and livenbr == 3:
                    board[row][col] = 2
                
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] >=1:
                    board[row][col] =1
                else:
                    board[row][col] = 0