from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li = []
        tmp = ''
        for x in s:
            if x not in tmp:
                tmp += x
            else:
                li.append(len(tmp))
                tmp = tmp[tmp.index(x)+1:] + x
        li.append(len(tmp))
        return max(li)
