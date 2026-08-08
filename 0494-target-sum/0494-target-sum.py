class Solution:
    def soln(self,i,target,nums,dp):
        if i==-1:
            if target==0:
                return 1
            return 0
        if dp[i][target]!=-1:
            return dp[i][target]
        p=self.soln(i-1,target-nums[i],nums,dp)
        n=self.soln(i-1,target+nums[i],nums,dp)
        dp[i][target]=p+n
        return dp[i][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if not -total<=target<=total:
            return 0
        dp=[[-1 for _ in range(-total,total+1)] for _ in range(len(nums))]
        return self.soln(len(nums)-1,target,nums,dp)