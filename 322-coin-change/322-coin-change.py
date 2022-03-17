class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX_INT = 100000
        if amount == 0:
            return 0
        
        if amount in coins:
            return 1
        
        dp = [MAX_INT]*(amount+1)
        dp[0] = 0
        dp[1] = 1 if 1 in coins else -1
        
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                minValForAllCoins = MAX_INT
                for coin in coins:
                    if i >= coin:
                        minValForAllCoins = min(dp[i-coin] + 1, minValForAllCoins)
                        
                dp[i] = minValForAllCoins
                        
        return dp[-1] if dp[-1] != MAX_INT else -1