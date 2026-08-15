class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = reduce(lambda a, b: a ^ b, nums)

        if total_xor != 0:
            return len(nums)

        if any(x != 0 for x in nums):
            return len(nums) - 1

        return 0


        # n=len(nums)
        # result=0
        # for x in range(1,1<<n):

        #     xor=0
        #     count=0
        #     while x>0:
        #         # print(x)
        #         lowest_set_bit = x & (-x)
        #         idx = lowest_set_bit.bit_length() - 1
        #         xor=xor^nums[idx]
        #         x=x&(x-1)
        #         count+=1

        #     # print(" ")
        #     if xor!=0:
        #         result=max(result,count)

        # return result