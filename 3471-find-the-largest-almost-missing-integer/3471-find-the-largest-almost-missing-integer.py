class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        if k==1:
            result=-1
            for x in nums:
                if freq[x]==1:
                    result=max(result,x)
            return result
        if k>1 and len(nums)>2 and k<len(nums):
            if nums[0]<nums[-1]:
                nums[0],nums[-1]=nums[-1],nums[0]
            if freq[nums[0]]==1:
                return nums[0]
            if freq[nums[-1]]==1:
                return nums[-1]
            return -1
        return max(nums)