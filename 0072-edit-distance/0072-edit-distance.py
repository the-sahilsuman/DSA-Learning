class Solution:
    def soln(self,i,j,word1,word2):
        if i<0:
            return j+1
        if j<0:
            return i+1

        if word1[i]==word2[j]:
            return self.soln(i-1,j-1,word1,word2)
        else:
            return 1+min(self.soln(i-1,j,word1,word2),self.soln(i,j-1,word1,word2),self.soln(i-1,j-1,word1,word2))

    def minDistance(self, word1: str, word2: str) -> int:
        # if not word1:
        #     return len(word2)
        # if not word2:
        #     return len(word1)

        # return self.soln(len(word1)-1,len(word2)-1,word1,word2)


        n=len(word1)
        m=len(word2)

        dp=[[0]*(n+1) for _ in range(m+1)]
        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters into word1


        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[j-1]==word2[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        
        return dp[m][n]
            
