class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words=set(wordDict)

        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True

        for i in range(1,n+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in words:
                    dp[i]=True
                    break

        return dp[n]


        # n=len(s)
        
        # def check(i,j):
        #     if i==n:
        #         return True
        #     if j==n-1:
        #         return True if s[i:j+1] in wordDict else False
            
        #     temp=s[i:j+1]
        #     if temp in wordDict:
        #         i=j=j+1
        #         return check(i,j)
        #     else:
        #         return check(i,j+1)

        # return check(0,0)
