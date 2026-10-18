class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1

        for x in range(2,n+1):
            for y in range(1,x):
                dp[x] = max(dp[x], y * (x - y), dp[y] * (x - y))
        return dp[n]