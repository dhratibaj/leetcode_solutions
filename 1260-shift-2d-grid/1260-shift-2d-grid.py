class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        a=[]
        ans1=[]
        ans=[]
        c=0
        if m==1 and n==1:
            return grid
        for i in range(m):
            for j in range(n):
                a.append(grid[i][j])
        l=len(a)
        for i in range(k):
            x=a[l-1]
            a.pop(l-1)
            a.insert(0,x)
        for i in range(l):
            if c==n:
                ans1.append(ans)
                ans=[]
                c=0
            ans.append(a[i])
            c+=1
        ans1.append(ans)
        return(ans1)