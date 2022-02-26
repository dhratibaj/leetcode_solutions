class Solution:
    def fib(self, n: int) -> int:
        F = {0:0, 1:1}
        if n < 2:
            return F[n]
        else:                               
            for i in range(2,n):
                F[i] = F[i-1] + F[i-2]
        return F[n-1] + F[n-2]
        
        #1520ms Runtime and 13.8 MB
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)