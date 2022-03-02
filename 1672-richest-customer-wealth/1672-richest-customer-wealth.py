class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            c = 0
            for j in range(len(accounts[i])):
                c += accounts[i][j]
            ans = max(ans,c)
        return ans