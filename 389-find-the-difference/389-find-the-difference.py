class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1,d2={},{}
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i]=1
        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i]=1
        for i in d2:
            if i in d1:
                if d1[i] != d2[i]:
                    return i
        return i