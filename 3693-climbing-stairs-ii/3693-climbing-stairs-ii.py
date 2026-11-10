class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        result=[float("inf") for _ in range(n+1)]
        result[0]=0

        for i in range(1,n+1):
            if i-1>-1:
                result[i]=min(result[i],result[i-1]+costs[i-1]+1)
            if i-2>-1:
                result[i]=min(result[i],result[i-2]+costs[i-1]+4)
            if i-3>-1:
                result[i]=min(result[i],result[i-3]+costs[i-1]+9)

        
        return result[n]