class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if m == 1 and n == 1:
            return 1

        row_heaps = [[] for _ in range(m)]
        col_heaps = [[] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                
                while row_heaps[i] and row_heaps[i][0][1] < j:
                    heapq.heappop(row_heaps[i])
                
                while col_heaps[j] and col_heaps[j][0][1] < i:
                    heapq.heappop(col_heaps[j])

                if i == 0 and j == 0:
                    curr_dp = 1
                else:
                    curr_dp = float('inf')
                    if row_heaps[i]:
                        curr_dp = min(curr_dp, row_heaps[i][0][0] + 1)
                    if col_heaps[j]:
                        curr_dp = min(curr_dp, col_heaps[j][0][0] + 1)

                if i == m - 1 and j == n - 1:
                    return curr_dp if curr_dp != float('inf') else -1

                if curr_dp != float('inf') and grid[i][j] > 0:
                    heapq.heappush(row_heaps[i], (curr_dp, j + grid[i][j]))
                    heapq.heappush(col_heaps[j], (curr_dp, i + grid[i][j]))

        return -1


        # m=len(grid)
        # n=(len(grid[0]))
        
        # dp=[[sys.maxsize]*n for _ in range(m)]
        # dp[m-1][n-1]=1

        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if i==m-1 and j==n-1:
        #             continue
        #         # temp=sys.maxsize
        #         for x in range(1,grid[i][j]+1):
        #             if 0<=j+x<n:
        #                 dp[i][j]=min(dp[i][j],1+dp[i][j+x])
        #             if 0<=i+x<m:
        #                 dp[i][j]=min(dp[i][j],1+dp[i+x][j])
                
        # # print(dp)       
        # return dp[0][0] if dp[0][0] != sys.maxsize else -1