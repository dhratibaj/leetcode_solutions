class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        for i in range(len(s)):
            if s[i] not in s[start:i]:
                max_len = max(max_len, i+1-start)
            else:
                start+=(1+s[start:i].index(s[i]))
        return(max(max_len, len(s)-start))