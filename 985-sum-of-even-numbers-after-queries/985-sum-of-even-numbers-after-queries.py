class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l = []
        summ = 0
        for x in nums:
            if not x&1:
                summ += x
        for i,j in queries:
            if(not nums[j]&1): summ-=nums[j]
            nums[j] = nums[j] + i
            if(not nums[j]&1): summ += nums[j]
            l.append(summ)
        return l