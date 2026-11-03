class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        
        count=0
        max_val=0
        for idx,num in enumerate(nums):
            max_val=max(max_val,num)
            if locked[idx]==1:
                if num!=idx+1:
                    locked[idx]=0
                    count+=1
                else:
                    if max_val>num:
                        count+=1
                        locked[idx]=0

            if count>k:
                return -1
        n=len(nums)
        for i in range(n-1,-1,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    count+=1

        return count

        

        

        

        
