class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #Initialize list 
        dp = [0] * (target + 1)
		#Set base case
        dp[0] = 1
		#Iterate thru each possible sum up to target
        for total in range(1, target + 1):
			#For each number in input list, if in bounds add number of combinations up to (total - num)	
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total - num]
		#Return number of combinations up to target
        return dp[target]