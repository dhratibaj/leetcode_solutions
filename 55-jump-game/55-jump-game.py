class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gap = 0
        for i in range(len(nums) - 2, -1, -1):
            gap = 0 if nums[i] > gap else (gap + 1)
        return gap is 0
        
        # #''' Greedy Soln (Explore from End -> Start) '''
        # size = len(nums)
        # goal = size - 1 
        # for i in range(size-1, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0