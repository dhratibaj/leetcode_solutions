class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        out = []
        out.append([1])
        out.append([1,1])
        if numRows>2:            
            for i in range(2, numRows):
                arr = [0]*(i+1)
                arr[0] = 1
                arr[-1] = 1                
                for j in range(1, i):                    
                    arr[j] = out[i-1][j-1] + out[i-1][j]                    
                out.append(arr)
        return out