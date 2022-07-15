class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact,nums = 1,[]
        for i in range(1,n):
            fact *= i
            nums.append(i)
        nums.append(n)
        ans = ""
        k -= 1
        while(True):
            ans += str(nums[k//fact])
            nums.remove(nums[k//fact])
            if len(nums) == 0: break
            k %= fact
            fact //= len(nums)
        return ans