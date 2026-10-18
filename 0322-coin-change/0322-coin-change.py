class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0

        for amt in range(1,amount+1):
            for coin in coins:
                if coin<=amt and dp[amt-coin]<dp[amt]:
                    dp[amt]=dp[amt-coin]+1
        

        return dp[amount] if dp[amount]!=float("inf") else -1