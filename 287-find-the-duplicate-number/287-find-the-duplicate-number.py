class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
                return i
            else:
                d[i]=1


# from collections import Counter
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         a = Counter(nums)
#         for i in a:
#             if a[i]>1:
#                 return i