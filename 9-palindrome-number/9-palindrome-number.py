class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if x<0:
            return True if s=='-'+s[::-1] else False
        return True if s==s[::-1] else False