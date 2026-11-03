class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val=max(nums)
        count=0
        for x in nums:
            count+=(max_val-x)

        return count