class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        matrix=[]
        top=left=0
        count=0
        bot=right=n-1
        for i in range(n):
            a=[]
            for j in range(n):
                a.append(0)
            matrix.append(a)
        
        while(count<n*n):
            for i in range(left,right+1):
                if count<n*n:
                    count+=1
                    matrix[top][i]=count
            top+=1
            for i in range(top,bot+1):
                if count<n*n:
                    count+=1
                    matrix[i][right]=count
            right-=1
            for i in range(right,left-1,-1):
                if count<n*n:
                    count+=1
                    matrix[bot][i]=count
            bot-=1
            for i in range(bot,top-1,-1):
                if count<n*n:
                    count+=1
                    matrix[i][left]=count
            left+=1
        return matrix