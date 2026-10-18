class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways_to_interleave = math.comb(len(left) + len(right), len(left))
            
            left_ways = dfs(left)
            right_ways = dfs(right)
            
            return ways_to_interleave * left_ways * right_ways
        
        return (dfs(nums) - 1) % MOD