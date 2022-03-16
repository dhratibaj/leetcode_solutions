class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #---------------------Greedy---------------------------
        profit, curr_min = 0, float("inf")
		
        for p in prices:
            curr_min = min(curr_min, p)
            
            if p - curr_min - fee > 0:
                profit += (p - curr_min - fee)
                curr_min = p - fee
        
        return profit
        
        #--------------DP----------------------------------------
#         memo = {}
#         def dp(i, buy):
#             if i == len(prices):
#                 return 0
            
#             key = (i, buy)
#             if key in memo:
#                 return memo[key]
            
#             profit = dp(i+1, buy)
#             if buy:
#                 profit = max(profit, dp(i+1, not buy) - prices[i])
#             else:
#                 # If selling then also consider the transaction fee of selling
#                 profit = max(profit, dp(i+1, not buy) + prices[i] - fee)
            
#             memo[key] = profit 
#             return profit
        
#         return dp(0, True)