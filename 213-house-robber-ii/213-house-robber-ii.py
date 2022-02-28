class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        res1 = [0,0]
        for num in nums[1:]:
            res1[0], res1[1] = res1[1], max(res1[0] + num, res1[1])   
        res2 = [0,0]
        for num in nums[:-1]:
            res2[0], res2[1] = res2[1], max(res2[0] + num, res2[1])  
        return max(res1[1], res2[1]) 