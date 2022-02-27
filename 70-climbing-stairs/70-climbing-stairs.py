class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        return self.dp(n, memo)
        
    def dp(self, n, memo):
        if n in memo:
            return memo[n]
        memo[n] = self.dp(n - 2, memo) + self.dp(n - 1, memo)
        return memo[n]