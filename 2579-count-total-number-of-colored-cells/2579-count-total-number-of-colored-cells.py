class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 5
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=5
        for x in range(3,n+1):
            diff=dp[x-1]-dp[x-2]
            dp[x]=dp[x-1]+diff+4
        return dp[n]