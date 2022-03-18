class Solution:
    def check(self,n,ans,max_num):
        if ans>min(self.ans_lst):
            return
        if n == 0:
            self.ans_lst.append(ans)
        for i in range(min(max_num,int(n**0.5)),0,-1): 
            if (min(self.ans_lst)-ans)*i**2 <= n:
                break
            if ans<min(self.ans_lst):
                n1 =n - i**2
                self.check(n1,ans+1,i) 
    def numSquares(self, n: int) -> int:
        self.ans_lst = [float('inf')]
        self.check(n,0,float('inf')) 
        return min(self.ans_lst)