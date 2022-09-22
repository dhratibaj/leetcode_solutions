class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        l = s.split()
        for i in l:
            res+=(i[::-1])
            res+=' '
        return res[:len(res)-1]