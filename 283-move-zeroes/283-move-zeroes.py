class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
                continue
            nums[i-count]=nums[i]
        for i in range(len(nums)-count,len(nums)):
            nums[i]=0      