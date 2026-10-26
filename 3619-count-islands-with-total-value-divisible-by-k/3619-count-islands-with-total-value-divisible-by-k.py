class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0

            visited[i][j]=1

            if grid[i][j]==0:
                return 0

            pick=grid[i][j]
            for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=m or nj>=n:
                    continue
                if visited[ni][nj]==-1:
                    pick+=dfs(ni,nj)
            
            return pick

        visited=[[-1]*n for _ in range(m)]

        count=0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==-1 and grid[i][j]!=0:
                    if dfs(i,j)%k==0:
                        count+=1
        
        return count
