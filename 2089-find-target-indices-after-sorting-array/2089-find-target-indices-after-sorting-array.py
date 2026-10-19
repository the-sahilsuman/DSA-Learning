class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_count = 0
        equal_count = 0
        
        # Count numbers smaller than target and equal to target
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                equal_count += 1
                
        # The target indices will start exactly after all smaller elements
        return [less_count + i for i in range(equal_count)]