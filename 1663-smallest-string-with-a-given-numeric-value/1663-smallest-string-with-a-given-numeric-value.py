class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        diff = k - n
        q = diff // 25
        r = diff % 25
        ans = "a"*(n-q-1) + chr(97+r) + "z"*q if r else "a"*(n-q)+ "z"*q
        return ans