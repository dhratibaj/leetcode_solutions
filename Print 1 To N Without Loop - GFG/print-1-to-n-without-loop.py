#User function Template for python3

class Solution:
    x = 1
    def printNos(self,N):
        if self.x > N:
            return
        else:
            print(self.x,end=" ")
            self.x += 1
            self.printNos(N)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends