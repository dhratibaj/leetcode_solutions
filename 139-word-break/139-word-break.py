from typing import List
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Turn word dict into a set for O(1) lookups
        wordDict = set(wordDict)

        # Keep a set of possible lengths for all words in dict
        lens = set()
        for w in wordDict:
            lens.add(len(w))

        # DP list - i-th index = reached i-th letter in s
        # True = reachable, False = unreachable
        dp = [False for _ in range(len(s) + 1)]
        # Base case where 0 letters is reachable
        dp[0] = True

        for i in range(len(s)):
            # At each letter, check if it is reachable
            if dp[i] == True:
                # If current letter reached, we loop through looking ahead each length
                # and see if next l letters forms a word in wordDict
                for l in lens:
                    # handle case where we reach end. We can break early and return True
                    if i+l == len(s) and s[i:i+l] in wordDict:
                        return True

                    # Handle case where next l letters in wordDict but we haven't reached end
                    # Set look ahead DP to True
                    elif i+l < len(s) and s[i:i+l] in wordDict:
                        dp[i+l] = True
        
        return False