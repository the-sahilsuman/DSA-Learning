class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        max_index=nums.index(max(nums))
        min_index=nums.index(min(nums))
        print(max_index,min_index)

        n=len(nums)
        mid=n//2
        if (max_index<mid and min_index<mid):
            return max(min_index,max_index)+1
        if (max_index>=mid and min_index>=mid):
            return n-min(min_index,max_index)
        
        # print("diff")
        return min(min(min_index+1,n-min_index)+min(max_index+1,n-max_index),min(min_index+1,n-min_index,max_index+1,n-max_index)+abs(max_index-min_index))