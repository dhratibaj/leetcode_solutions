class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0]=='-':
            s = s[1:]
            rev_str = int('-'+s[::-1])
        else: rev_str = int(s[::-1])
        if rev_str>=(-2**31) and rev_str <=(2**31-1):
            return rev_str
        else: return 0