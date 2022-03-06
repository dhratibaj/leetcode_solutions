class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(n * 2) >> n) % (10**9 + 7)
        
        #------------------------------------------------------------
        # if n == 1:
        #     return 1
        # else:
        #     return (n*(2*n-1)*self.countOrders(n-1))%(10**9+7)