class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        
        for core in range(1, n + 1):
            current_sum = 0
            v = 1
            
            while core * (v * v) <= n:
                current_sum += nums[core * (v * v) - 1]
                v += 1
                
            max_sum = max(max_sum, current_sum)
            
        return max_sum




        # n=len(nums)

        # result=0
        # for x in range(2,n,2):
        #     print(x)
        #     if x&1:
        #         if x**2<=n:
        #             result=max(result,nums[0]+nums[(x**2)-1])
        #         continue
        #     for i in range(1,x):
        #         if (x**2)%i==0 and (x**2)//i<=n:
        #             # print(i,(x**x)//i)
        #             print(x**2,i,(x**2)/i,nums[i-1]+nums[((x**2)//i)-1])
        #             result=max(result,nums[i-1]+nums[((x**2)//i)-1])

        # return result