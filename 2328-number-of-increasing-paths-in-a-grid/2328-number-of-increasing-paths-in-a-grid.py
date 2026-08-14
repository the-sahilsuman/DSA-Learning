class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        memo = {}
        
        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            
            total_paths = 1
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    total_paths = (total_paths + dfs(nr, nc)) % MOD
            
            memo[(r, c)] = total_paths
            return total_paths
        
        ans = sum(dfs(r, c) for r in range(m) for c in range(n)) % MOD
        return ans