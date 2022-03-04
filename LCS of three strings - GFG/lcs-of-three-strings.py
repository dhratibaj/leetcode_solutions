#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
    #     memo=[[[-1]*(n3+1) for i in range(n2+1)] for  i in range(n1+1)]
    #     return self.solve(A,B,C,0,0,0,n1,n2,n3,memo)
    # def solve(self,A,B,C,i,j,k,n1,n2,n3,memo):
    #     if (i == n1 or j == n2 or k == n3):
    #         return 0
    #     if (memo[i][j][k] != -1):
    #         return memo[i][j][k]
    #     if (A[i] == B[j] and A[i] == C[k]):
    #         memo[i][j][k] = 1 + self.solve (A, B, C, i + 1, j + 1, k + 1, n1, n2, n3,memo);
    #         return memo[i][j][k]
    #     memo[i][j][k] = max (self.solve (A, B, C, i + 1, j, k, n1, n2, n3,memo),
    #                                  self.solve (A, B, C, i, j + 1, k, n1, n2, n3,memo),
    #                                  self.solve (A, B, C, i, j, k + 1, n1, n2, n3,memo),
    #                                  self.solve (A, B, C, i + 1, j + 1, k, n1, n2, n3,memo),
    #                                  self.solve (A, B, C, i + 1, j, k + 1, n1, n2, n3,memo),
    #                                  self.solve (A, B, C, i, j + 1, k + 1, n1, n2, n3,memo));
    #     return memo[i][j][k]
        #--------------------------------------------------------------------------------
        L = [[[0 for i in range(n3+1)] for j in range(n2+1)]for k in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                for k in range(n3+1):
                    if i==0 or j==0 or k==0:
                        L[i][j][k] = 0
                    elif (A[i-1] == B[j-1] and A[i-1] == C[k-1]):
                        L[i][j][k] = L[i-1][j-1][k-1] + 1
                    else:
                        L[i][j][k] = max(max(L[i-1][j][k],L[i][j-1][k]),L[i][j][k-1])
        return L[n1][n2][n3]
        #---------------------------------------------------------------------------------
        # def lcs(s1,s2):
        #     n,m = len(s1),len(s2)
        #     dp = [[-1 for i in range(m+1)]for j in range(n+1)]
        #     for i in range(n+1):
        #         dp[i][0] = 0
        #     for j in range(m+1):
        #         dp[0][j] = 0
        #     for i in range(1,n+1):
        #         for j in range(1,m+1):
        #             if s1[i-1] == s2[j-1]:
        #                 dp[i][j] = 1+dp[i-1][j-1]
        #             else:
        #                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        #     return dp[-1][-1]
            
        # return min(lcs(A,B),lcs(B,C),lcs(C,A))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends