#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        total = (n + 1)*(n)//2
        sum_of_A = sum(array)
        return total - sum_of_A
        
        #------- gives TLE
        # for i in range(1,n+1):
        #     if i not in array:
        #         return i

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends