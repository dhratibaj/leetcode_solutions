class Solution:
    def rob(self, nums: List[int]) -> int:
        # s1,s2 = 0,0
        # for i in range(0,len(nums),2):
        #     s1 += nums[i]
        # for i in range(1,len(nums),2):
        #     s2 += nums[i]
        # return max(s1,s2)
            
        last, now = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)
        return now