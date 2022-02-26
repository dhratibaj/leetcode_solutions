class Solution:
    def tribonacci(self, n: int) -> int:
        F = {0:0,1:1,2:1}
        if n < 3:
            return F[n]
        else:
            for i in range(3,n):
                F[i] = F[i-3]+F[i-2]+F[i-1]
        return F[n-1]+F[n-2]+F[n-3]
                