class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        memo = {}
        m, n = len(grid), len(grid[0])
        
        def dp(i, j):
            if i == m or j == n or grid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            key = (i, j)
            if key in memo:
                return memo[key]
            
            right = dp(i, j+1)
            bottom = dp(i+1, j)
            memo[key] = right + bottom
            
            return memo[key]
        
        return dp(0, 0)