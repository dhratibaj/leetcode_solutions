class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1: return True
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i-1] < i: 
                dp[i] = dp[i-1] 
            else:
                dp[i] = max(dp[i-1], nums[i]+i) 
        return dp[-1] >= n-1
        
        #----------------------------------------------
        # gap = 0
        # for i in range(len(nums) - 2, -1, -1):
        #     gap = 0 if nums[i] > gap else (gap + 1)
        # return gap is 0
        
        #-----------------------------------------------------
        # #''' Greedy Soln (Explore from End -> Start) '''
        # size = len(nums)
        # goal = size - 1 
        # for i in range(size-1, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0