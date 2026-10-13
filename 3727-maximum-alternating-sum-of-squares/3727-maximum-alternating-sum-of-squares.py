class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=list(map(lambda x:abs(x),nums))
        nums.sort(reverse=True)
        n=len(nums)
        mid=n//2+1 if n&1==1 else n//2

        result=0
        for i in range(n):
            if i<mid:
                result+=pow(nums[i],2)
            else:
                result-=pow(nums[i],2)

        return result