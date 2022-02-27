def longest(s,n):
    dp = [[False]*(n+1)for i in range(n+1)]
    for g in range(0,n):
        i,j = 0,g
        while i<n and j<n:
            if g == 0:
                dp[i][j]=True
            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=True
            else:
                if s[i]==s[j] and dp[i+1][j-1]==True: 
                    dp[i][j]=True
            i += 1
            j += 1
    count = 0
    for i in range(n+1):
        for j in range(n+1):
            if dp[i][j]:
                count+=1
    return count

class Solution:
    def countSubstrings(self, s: str) -> str:
        return longest(s,len(s))