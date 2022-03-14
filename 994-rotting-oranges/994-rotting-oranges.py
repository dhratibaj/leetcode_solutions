class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0
        fresh = 0
        rotten_oranges = list()
        
        for r_idx, row in enumerate(grid):
            for c_idx, orange in enumerate(row):
                if orange == 1:
                    fresh += 1
                elif orange == 2:
                    rotten_oranges.append((r_idx, c_idx))
        
        def fresh_neighbors(r, c, grid):
            for r_d, c_d in DIRECTIONS:
                new_r = r + r_d
                new_c = c + c_d
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                    yield new_r, new_c
            
        
        def time_elapse(grid, rotten_oranges):
            new_rotten = list()
            for r, c in rotten_oranges:
                for neighbor_r, neighbor_c in fresh_neighbors(r, c, grid):
                    grid[neighbor_r][neighbor_c] = 2
                    new_rotten.append((neighbor_r, neighbor_c))
            return new_rotten
        
        # simulate the rotten procedure
        # if the rotten orange doesn't increase
            # if all the orange has rotten, return time
            # if there remains some orange, return -1
        # else, increase time
        
        while True:
            rotten_oranges = time_elapse(grid, rotten_oranges)
            fresh -= len(rotten_oranges)
            if rotten_oranges:
                time += 1
            else:
                if fresh:
                    return -1
                else:
                    return time