class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n,m = len(word1),len(word2)
        if n <= m:
            for i in range(n):
                res += word1[i]+word2[i]
            for i in range(n,m):
                res+=word2[i]
            return res
        else:
            for i in range(m):
                res += word1[i]+word2[i]
            for i in range(m,n):
                res+=word1[i]
            return res