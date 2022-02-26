class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(res, self.substring(s, i, i), self.substring(s, i, i+1), key=len)
        return res
    
    def substring(self, s, l , r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]