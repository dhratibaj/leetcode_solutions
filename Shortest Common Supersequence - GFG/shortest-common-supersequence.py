#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        def lcs(x, y):
            dp = [[-1 for i in range(len(y)+1)]for j in range(len(x)+1)]
            for i in range(len(x)+1):
                dp[i][0] = 0
            for j in range(len(y)+1):
                dp[0][j] = 0
            for i in range(1,len(x)+1):
                for j in range(1,len(y)+1):
                    if x[i-1] == y[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[-1][-1]
        
        return m + n - lcs(X,Y)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends