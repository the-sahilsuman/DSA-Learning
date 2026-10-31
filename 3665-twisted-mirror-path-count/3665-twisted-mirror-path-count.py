from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # dest[r][c][0] = final resting cell if entering (r, c) moving RIGHT
        # dest[r][c][1] = final resting cell if entering (r, c) moving DOWN
        dest = [[[None, None] for _ in range(n)] for _ in range(m)]
        
        # ways[r][c] = number of valid paths to the end from cell (r, c)
        ways = [[0] * n for _ in range(m)]
        ways[m - 1][n - 1] = 1
        
        # Traverse backwards to compute both reflections and path counts
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Base case: The destination cell immediately stops the robot
                if r == m - 1 and c == n - 1:
                    dest[r][c][0] = (r, c)
                    dest[r][c][1] = (r, c)
                    continue
                    
                # Precompute destinations for entering this cell
                if grid[r][c] == 0:
                    dest[r][c][0] = (r, c)
                    dest[r][c][1] = (r, c)
                else:
                    # Mirror: Moving RIGHT reflects DOWN to (r+1, c)
                    if r + 1 < m:
                        dest[r][c][0] = dest[r + 1][c][1]
                    # Mirror: Moving DOWN reflects RIGHT to (r, c+1)
                    if c + 1 < n:
                        dest[r][c][1] = dest[r][c + 1][0]
                        
                # Calculate paths from this cell (we only make decisions from empty cells or the start)
                if (r == 0 and c == 0) or grid[r][c] == 0:
                    paths = 0
                    
                    # Try moving RIGHT
                    if c + 1 < n:
                        target = dest[r][c + 1][0]
                        if target:
                            paths = (paths + ways[target[0]][target[1]]) % MOD
                            
                    # Try moving DOWN
                    if r + 1 < m:
                        target = dest[r + 1][c][1]
                        if target:
                            paths = (paths + ways[target[0]][target[1]]) % MOD
                            
                    ways[r][c] = paths
                    
        return ways[0][0]