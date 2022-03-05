from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        count = {node: 0 for node in range(0, max(nums) + 1)}
        for num in nums:
            count[num] += 1
        def dp(k: int) -> int:
            if k == 0:
                return 0
            if k == 1:
                return count[1]
            if not k in memo:
                memo[k] = max(dp(k - 2) + count[k] * k, dp(k - 1))
            return memo[k]
        return dp(max(nums))