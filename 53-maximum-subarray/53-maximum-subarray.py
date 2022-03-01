class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum,res =0,nums[0]
        for i in nums:
            if sum<0:
                sum = 0
            sum += i
            res = max(res,sum)
        return res
                