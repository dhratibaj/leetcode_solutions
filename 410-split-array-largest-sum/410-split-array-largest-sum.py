class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        while low < high:
            mid = low + (high - low) // 2
            if self.getSubArrayCounts(nums, mid) > m:
                low = mid + 1
            else:
                high = mid
        return low
    
    def getSubArrayCounts(self, nums, capacity):
        counts, currentCapacity = 0, 0
        for n in nums:
            if currentCapacity - n < 0:
                currentCapacity = capacity - n
                counts += 1
            else:
                currentCapacity -= n
        return counts