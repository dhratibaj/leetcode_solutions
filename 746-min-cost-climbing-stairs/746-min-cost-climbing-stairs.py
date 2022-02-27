class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        if len(cost) >= 1:
            dp.append(0)
        if len(cost) >= 2:
            dp.append(0)
        for i in range(2,len(cost)+1):
            dp.append(min(dp[i-2] + cost[i-2],dp[i-1]+cost[i-1]))
        return dp[-1]