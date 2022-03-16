class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i, buy):
            if i == len(prices):
                return 0
            
            key = (i, buy)
            if key in memo:
                return memo[key]
            
            profit = dp(i+1, buy)
            if buy:
                profit = max(profit, dp(i+1, not buy) - prices[i])
            else:
                # If selling then also consider the transaction fee of selling
                profit = max(profit, dp(i+1, not buy) + prices[i] - fee)
            
            memo[key] = profit 
            return profit
        
        return dp(0, True)