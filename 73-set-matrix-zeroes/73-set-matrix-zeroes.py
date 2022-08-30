class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l.append([i,j])
        for i in range(len(l)):
            for j in range(len(matrix[0])):
                matrix[l[i][0]][j] = 0
        for i in range(len(l)):
            for j in range(len(matrix)):
                matrix[j][l[i][1]] = 0