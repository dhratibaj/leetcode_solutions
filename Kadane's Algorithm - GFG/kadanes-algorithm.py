class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max_so_far =arr[0]
        curr_max = arr[0]
     
        for i in range(1,N):
            curr_max = max(arr[i], curr_max + arr[i])
            max_so_far = max(max_so_far,curr_max)
         
        return max_so_far
        
        # ans, res = 0, arr[0]
        # for i in arr:
        #     if ans<0:
        #         ans = 0
        #     ans+=i
        #     res = max(res,ans)
        # if ans<0:
        #     return -1
        # return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends