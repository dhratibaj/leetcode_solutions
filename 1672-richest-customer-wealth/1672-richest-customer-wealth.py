class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        for l in accounts:
            maxx = max(maxx,sum(l))
        return maxx