class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        rows=[0]*m
        columns=[0]*n

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows[i]+=1
                    columns[j]+=1
                    count+=1

        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (rows[i]>1 or columns[j]>1):
                    count+=1

        return count