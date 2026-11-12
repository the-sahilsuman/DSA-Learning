class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)

        result=1
        i=1
        while i<n:
            count=1
            if nums[i]>nums[i-1]:
                while i<n and nums[i]>nums[i-1]:
                    count+=1
                    i+=1
                # result=max(result,count)
            
            elif nums[i]<nums[i-1]:
                while i<n and nums[i]<nums[i-1]:
                    count+=1
                    i+=1
                # result=max(result,count)

            else:
                i+=1

            result=max(result,count)
            
        return result
            
        
            
            