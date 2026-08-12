class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result=0
        freq={}
        start,end=0,0
        while start<=end and end<len(nums):

            while end<len(nums):
                if nums[end] in freq:
                    if freq[nums[end]]<k:
                        freq[nums[end]]+=1
                    else:
                        break
                else:
                    freq[nums[end]]=1
                end+=1
            result=max(result,end-start)
            
            freq[nums[start]]-=1
            start+=1
                    
        return result