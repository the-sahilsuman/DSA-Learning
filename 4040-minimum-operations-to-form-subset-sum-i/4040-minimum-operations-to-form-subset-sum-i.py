class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        INF = float("inf")
        target_sum=sum
        dp = [INF] * (target_sum + 1)
        dp[0] = 0

        for x in nums:
            options = {}

            curr, cost = x, 0
            while True:
                if curr <= target_sum:
                    if curr not in options or cost < options[curr]:
                        options[curr] = cost
                if curr == 0:
                    break
                curr //= 2
                cost += 1

            if x > 0:
                curr, cost = x, 0
                while curr <= target_sum:
                    if curr not in options or cost < options[curr]:
                        options[curr] = cost
                    curr *= 2
                    cost += 1

            next_dp = list(dp)
            for val, cost in options.items():
                if val == 0:
                    continue
                for s in range(val, target_sum + 1):
                    if dp[s - val] != INF:
                        if dp[s - val] + cost < next_dp[s]:
                            next_dp[s] = dp[s - val] + cost

            dp = next_dp

        return dp[target_sum] if dp[target_sum] != INF else -1





















        # # nums.sort()
        # def soln(i,val):
        #     print(i,val)

        #     if val==0:
        #         return 0
        #     if val<0 or i>=len(nums):
        #         return float('inf')

        #     skip=soln(i+1,val)
        #     plan=soln(i+1,val-nums[i])

        #     temp=nums[i]
        #     multi=float('inf')
        #     ops = 0
        #     while temp<val:
        #         multi=min(multi,ops+soln(i+1,val-temp*(power(2,ops))))
        #         ops+=1

        #     temp=nums[i]//2
        #     div=float('inf')
        #     ops = 1
        #     while temp>1:    
        #         div=min(div,ops+soln(i+1,val-temp))
        #         temp//=2
        #         ops+=1

        #     return min(skip,plan,multi,div)

        # res=soln(0,sum)
        # return res if res != float('inf') else -1
