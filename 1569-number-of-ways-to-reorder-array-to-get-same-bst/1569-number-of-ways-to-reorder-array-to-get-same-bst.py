import math
class Solution:
    def numOfWays(self, a: List[int]) -> int:
        def func(nums):
            if len(nums)<=2:
                return 1
            root = nums[0]
            l1,l2=[],[]
            for i in range(1,len(nums)):
                if nums[i]<root:
                    l1.append(nums[i])
                elif nums[i]>root:
                    l2.append(nums[i])
            pl = func(l1)
            pr = func(l2)
            return math.factorial(len(nums)-1)* pl * pr//(math.factorial(len(l1))*math.factorial(len(l2)))
        return (func(a)-1) % 1000000007