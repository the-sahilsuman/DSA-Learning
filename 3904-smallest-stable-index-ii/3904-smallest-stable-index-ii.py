class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_arr=nums.copy()
        max_val=nums[0]
        for i in range(1,len(nums)):
            max_val=max(max_val,nums[i])
            max_arr[i]=max_val

        print(max_arr)

        min_arr=nums.copy()
        min_val=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            min_val=min(min_val,nums[i])
            min_arr[i]=min_val

        # result=-1
        for i in range(len(nums)):
            if max_arr[i]-min_arr[i]<=k:
                return i

        return -1