class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1: return True
        elif n<=0 or n%2!=0: return False
        return self.isPowerOfTwo(n//2)
        
        #-----------------1 line approach----------------------
        #return (n!=0) and (n&(n-1)==0)