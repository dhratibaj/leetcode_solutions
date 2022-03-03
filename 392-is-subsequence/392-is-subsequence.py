class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def lcs(s,t):
            n,m = len(s),len(t)
            dp = [[-1 for i in range(m+1)]for i in range(n+1)]
            for i in range(n+1):
                dp[i][0] = 0
            for i in range(m+1):
                dp[0][i] = 0
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if s[i-1] == t[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[-1][-1]
        
        return len(s) == lcs(s,t)
        
        #-----------------2nd approach
        # i,j=0,0
        # while(j<len(s) and i<len(t)):
        #     if(s[j]==t[i]):
        #         j+=1
        #     i+=1
        # return j==len(s)