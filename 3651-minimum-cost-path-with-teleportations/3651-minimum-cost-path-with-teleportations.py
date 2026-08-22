class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid),len(grid[0])
        
        val_to_cells = defaultdict(list)
        for r in range(m):
            for c in range(n):
                val_to_cells[grid[r][c]].append((r, c))
                
        sorted_vals = sorted(val_to_cells.keys(), reverse=True)
        
        dp = [[sys.maxsize] * n for _ in range(m)]
        dp[0][0] = 0  
        
        for r in range(m):
            for c in range(n):
                if dp[r][c] == sys.maxsize:
                    continue
                if r + 1 < m:
                    dp[r + 1][c] = min(dp[r + 1][c], dp[r][c] + grid[r + 1][c])
                if c + 1 < n:
                    dp[r][c + 1] = min(dp[r][c + 1], dp[r][c] + grid[r][c + 1])
                    
        for _ in range(k):
            new_dp = [row[:] for row in dp]
            
            running_min = sys.maxsize
            for val in sorted_vals:
                cells = val_to_cells[val]
                for r, c in cells:
                    running_min = min(running_min, dp[r][c])
                for r, c in cells:
                    new_dp[r][c] = min(new_dp[r][c], running_min)
            
            for r in range(m):
                for c in range(n):
                    if new_dp[r][c] == sys.maxsize:
                        continue
                    if r + 1 < m:
                        new_dp[r + 1][c] = min(new_dp[r + 1][c], new_dp[r][c] + grid[r + 1][c])
                    if c + 1 < n:
                        new_dp[r][c + 1] = min(new_dp[r][c + 1], new_dp[r][c] + grid[r][c + 1])
            
            dp = new_dp
            
        return dp[m - 1][n - 1]