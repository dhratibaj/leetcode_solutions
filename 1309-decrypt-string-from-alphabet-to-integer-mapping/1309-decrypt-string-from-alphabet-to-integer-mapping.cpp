class Solution:
    def freqAlphabets(self, s: str) -> str:
        res,n = "",len(s)
        i = n-1
        while(i>=0):
            if s[i] == '#':
                res += chr(ord("a")+int(s[i-2:i])-1)
                i -= 3
            else:
                res += chr(ord("a") + int(s[i])-1)
                i -= 1
        return res[::-1]