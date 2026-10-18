class Solution:
    def soln(self,i,j,str1,str2):
        if i>=len(str1):
            return str2[j:]
        if j>=len(str2):
            return str1[i:]

        if str1[i]==str2[j]:
            return str1[i]+self.soln(i+1,j+1,str1,str2)
        else:
            s1=str1[i]+self.soln(i+1,j,str1,str2)
            s2=str2[j]+self.soln(i,j+1,str1,str2)
            if len(s1)>len(s2):
                return s2
            return s1

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # return self.soln(0,0,str1,str2)


        # LCS method
        m=len(str1)
        n=len(str2)
        
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
        result=[]
        i,j=m,n
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                result.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                result.append(str1[i-1])
                i-=1
            else:
                result.append(str2[j-1])
                j-=1

        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
            
        # The string was built backwards, so reverse and join
        return "".join(reversed(result))
