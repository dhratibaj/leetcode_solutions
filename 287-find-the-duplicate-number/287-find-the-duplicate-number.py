from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = Counter(nums)
        for i in a:
            if a[i]>1:
                return i