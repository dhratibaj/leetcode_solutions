#User function Template for python3
class Solution:
    def canMakeTriangle(self, A, N):
        out = []
        for i in range(N-2):
            a = A[i:i+3]
            if a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[1]+a[2]>a[0]:
                out.append(1)
            else:
                out.append(0)
        return out


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends