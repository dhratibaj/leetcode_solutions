class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for idx1 in reversed(range(len(nums) - 1)):
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx1] < nums[idx2]:
                    dp[idx1] = max(dp[idx1], dp[idx2] + 1)
        return max(dp)