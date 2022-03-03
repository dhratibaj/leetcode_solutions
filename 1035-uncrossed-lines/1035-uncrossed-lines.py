def solve(nums1,nums2,m,n):
    dp = [[-1 for i in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 0
    for i in range(n+1):
        dp[0][i] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if nums1[i-1]==nums2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        return solve(nums1,nums2,len(nums1),len(nums2))