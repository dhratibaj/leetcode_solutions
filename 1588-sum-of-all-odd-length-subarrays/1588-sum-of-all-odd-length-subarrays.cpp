class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = sum(arr)
        if len(arr)<3:
            return summ
        else:
            for i in range(3,len(arr)+1,2):
                j = 0
                while(j+i<=len(arr)):
                    summ += sum(arr[j:j+i])
                    j += 1
            return summ