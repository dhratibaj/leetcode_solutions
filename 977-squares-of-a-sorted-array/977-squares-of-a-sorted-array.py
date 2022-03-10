class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [x*x for x in nums]
        l.sort()
        return l
        # n = len(nums) - 1
        # l = []
        # i, j = 0, n
        # while(i<j):
        #     if nums[i] == 0:
        #         l.insert(0,0)
        #         i += 1
        #     elif nums[j] == 0:
        #         l.insert(0,0)
        #         j -= 1
        #     elif abs(nums[j])>abs(nums[i]):
        #         l.append(nums[i]*nums[i])
        #         i += 1
        #     elif abs(nums[j])<abs(nums[i]):
        #         l.append(nums[j]*nums[j])
        #         j -= 1
        #     elif abs(nums[i]) == abs(nums[j]):
        #         l.append(nums[i]*nums[i])
        #         l.append(nums[i]*nums[i])
        #         i += 1
        #         j -= 1
        # return l