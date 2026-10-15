class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # O(N^2) iteration over all subarrays
        for i in range(n):
            distinct_elements = set()
            
            for j in range(i, n):
                distinct_elements.add(nums[j])
                count = len(distinct_elements)
                
                # Add the square of the distinct count
                total_sum += count * count
                
        return total_sum