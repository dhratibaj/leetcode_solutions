class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(text1,text2):
            n,m = len(text1),len(text2)
            dp = [[-1 for i in range(m+1)]for j in range(n+1)]
            for i in range(n+1):
                dp[i][0] = 0
            for j in range(m+1):
                dp[0][j] = 0
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if text1[i-1] == text2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[-1][-1]
        return lcs(s,s[::-1])