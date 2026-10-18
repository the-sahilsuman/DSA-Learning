class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # n=len(nums)
        # arr=nums.copy()
        # arr.sort()

        # next={}
        # for x in range(n):
        #     if x==n-1:
        #         next[arr[x]]=-1
        #     else:
        #         next[arr[x]]=arr[x+1]

        # for x in range(n):
        #     nums[x]=next[nums[x]]

        # return nums

        n=len(nums)
        # print(n)
        arr=[-1]*n

        for i in range(n):
        
            j=(i+1)%n
            while True:
                if j==i:
                    arr[i]=-1
                    break
                if nums[j]>nums[i]:
                    # print(i,j)
                    arr[i]=nums[j]
                    break
                j=(j+1)%n
        return arr