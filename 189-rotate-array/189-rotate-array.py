class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if k == 0 or l == 1: return None
        if k > l: k = k % l
        nums[:] = nums[-k:] + nums[:l-k]