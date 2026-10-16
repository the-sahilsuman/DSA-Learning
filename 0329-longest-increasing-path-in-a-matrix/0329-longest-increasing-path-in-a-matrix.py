class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[-1]*n for _ in range(m)]

        # result=1
        # for _ in range(m):
        #     for i in range(m):
        #         for j in range(n):
        #             for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
        #                 ni=i+di
        #                 nj=j+dj
        #                 if 0<=ni<m and 0<=nj<n:
        #                     if matrix[ni][nj]>matrix[i][j]:
        #                         dp[i][j]=max(dp[ni][nj]+1,dp[i][j])
        #                         result=max(dp[i][j],result)
        
        # return result



        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=1
            for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni=i+di
                nj=j+dj
                if 0<=ni<m and 0<=nj<n:
                    if matrix[ni][nj]>matrix[i][j]:
                        dp[i][j]=max(dfs(ni,nj)+1,dp[i][j])
            return dp[i][j]

        result=1
        for i in range(m):
            for j in range(n):
                if dp[i][j]==-1:
                    temp=dfs(i,j)
                    result=max(result,temp)
                else:
                    result=max(result,dp[i][j])
        
        # print(dp)
        return result
                
        