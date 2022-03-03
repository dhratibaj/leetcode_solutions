class Solution:
    def rob(self, nums: List[int]) -> int:
        previous = current = 0
        for house in nums:
            previous, current = max(previous, current + house), previous
        return previous
        
        #-----------------1stApproach
        # s1,s2 = 0,0
        # for i in range(0,len(nums),2):
        #     s1 += nums[i]
        # for i in range(1,len(nums),2):
        #     s2 += nums[i]
        # return max(s1,s2)
        
        #-----------------2nd Approach
        # last, now = 0, 0
        # for i in nums: 
        #     last, now = now, max(last + i, now)
        # return now