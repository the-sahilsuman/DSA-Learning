class Solution:
    def rob(self, nums: list[int]) -> int:
        # n = len(nums)
        
        # def soln(i, status, dp):
        #     if i < 0:
        #         return 0
            
        #     if dp[i][status] != -1:
        #         return dp[i][status]
            
        #     if status == 1:
        #         pick = nums[i] + soln(i - 1, 0, dp)
        #         skip = soln(i - 1, 1, dp)
                
        #         dp[i][1] = max(pick, skip)
        #     else:
        #         dp[i][0] = soln(i - 1, 1, dp)

        #     return dp[i][status]
            
        # dp = [[-1] * 2 for _ in range(n)]
        
        # return soln(n - 1, 1, dp)


        n=len(nums)
        prev=[0]*2

        for i in range(n):
            curr=[0]*2
            for j in range(2):
                if j==0:
                    curr[0]=prev[1]
                else:
                    curr[1]=max(prev[0]+nums[i],prev[1])
                
            prev=curr
        
        return prev[1]



        # n=len(nums)
        # # result=0
        

        # def soln(i,total,status,dp):
        #     # nonlocal result
        #     if i==-1:
        #         return total
        #     if dp[i][status]!=-1:
        #         return dp[i][status]
        #     if status&1==1:
        #         dp[i][1]=max(dp[i][1],soln(i-1,total+nums[i],0,dp),soln(i-1,total,1,dp))
        #         # return dp[i][1]
        #     else:
        #         dp[i][0]=max(dp[i][0],soln(i-1,total,1,dp))

        #     return dp[i][status]
            
        
        # dp=[[-1]*2 for _ in range(n)]
        # pick=soln(n-1,0,1,dp)
        # return dp[n-1][1]