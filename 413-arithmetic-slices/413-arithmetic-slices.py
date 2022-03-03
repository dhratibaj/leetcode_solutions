class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        ans = 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1] + 1
                ans += dp[i]
        return ans
        
        
#         def num_ways(len):
#             return (len - 2) * (len - 1) // 2
            
#         result = 0
#         prev_delta = float("inf")
#         cur_len = 0
#         for i in range(1, len(nums)):
#             delta = nums[i] - nums[i - 1]
#             if delta == prev_delta:
#                 cur_len += 1
#             else:
#                 if cur_len >= 3:
#                     result += num_ways(cur_len)
#                 cur_len = 2
#                 prev_delta = delta
#         if cur_len >= 3:
#             result += num_ways(cur_len)

#         return result
        
        
#         if len(nums)<3:
#             return 0
#         elif len(nums)==3:
#             if (nums[1]-nums[0])!=(nums[2]-nums[1]):
#                 return 0
#             return 1
#         else:
#             c = nums[1]-nums[0]
#             for i in range(1,len(nums)-1):
#                 if (nums[i+1]-nums[i])!=c:
#                     return 0
#         n = len(nums)-2
#         return (n*(n+1))//2