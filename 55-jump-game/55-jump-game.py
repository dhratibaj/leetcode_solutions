class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #''' Greedy Soln (Explore from End -> Start) '''
        size = len(nums)
        goal = size - 1 
        for i in range(size-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0