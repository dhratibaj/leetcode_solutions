class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = 0
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                flag -= 1
        if flag%2==0:
            return 1
        else:
            return -1