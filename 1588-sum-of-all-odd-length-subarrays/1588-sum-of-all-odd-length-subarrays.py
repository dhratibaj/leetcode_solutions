class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(1,len(arr)+1,2):
            for k in range(len(arr)):
                if k+i > len(arr):
                        break
                else:
                    ans += sum(arr[k:k+i])
        return ans