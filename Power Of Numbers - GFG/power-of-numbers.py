#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        res = 1
        m = 1000000007
   
        while R>0:
            if R&1 != 0:
                res = (res * N%m) % m
            N = (N%m * N%m) % m
            R = R>>1
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends