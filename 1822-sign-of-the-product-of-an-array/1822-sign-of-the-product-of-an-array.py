class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = prod(nums)
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0