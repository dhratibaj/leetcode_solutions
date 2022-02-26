def longest(s,n):
    dp = [[False]*(n+1)for i in range(n+1)]
    for g in range(0,n):
        i,j = 0,g
        while i<n and j<n:
            if g == 0:
                dp[i][j]=True
                L = i
                R = j
            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=True
                    L = i
                    R = j
            else:
                if s[i]==s[j] and dp[i+1][j-1]==True: 
                    dp[i][j]=True
                    L = i
                    R = j
            i += 1
            j += 1
    return s[L:R+1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest(s,len(s))