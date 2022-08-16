class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = [i]
            else:
                a[s[i]].append(i)
        for i in a:
            if len(a[i])==1:
                return a[i][0]
        return -1