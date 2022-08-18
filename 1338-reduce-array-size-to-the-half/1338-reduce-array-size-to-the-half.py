from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter(arr)
        l = sorted(d.values())
        n = len(arr) // 2
        idx = 0
        while n > 0:
            n -= l[-idx-1]
            idx += 1  
        return idx