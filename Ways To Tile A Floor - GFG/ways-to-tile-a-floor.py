#User function Template for python3

class Solution:
    def numberOfWays(self, N):
        dp = [0]*100005
        dp[1] = 1
        dp[2] = 2
        for i in range(3,N+1):
            dp[i] = (dp[i-1]+dp[i-2])%1000000007
        
        return dp[N]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.numberOfWays(N))
# } Driver Code Ends