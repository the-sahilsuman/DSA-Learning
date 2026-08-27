class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        max_val = max(nums)
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def check(target_sum: int) -> bool:
            def dfs(u: int, parent: int) -> int:
                current_sum = nums[u]
                for neighbor in adj[u]:
                    if neighbor != parent:
                        child_res = dfs(neighbor, u)
                        if child_res == -1:
                            return -1
                        current_sum += child_res
                
                if current_sum > target_sum:
                    return -1
                if current_sum == target_sum:
                    return 0
                return current_sum
            
            return dfs(0, -1) == 0

        for num_components in range(n, 1, -1):
            if total_sum % num_components == 0:
                target_sum = total_sum // num_components
                if target_sum >= max_val and check(target_sum):
                    return num_components - 1
        
        return 0
        