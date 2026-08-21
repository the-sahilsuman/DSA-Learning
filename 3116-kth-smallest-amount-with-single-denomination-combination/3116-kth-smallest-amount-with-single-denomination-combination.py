class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        subsets = []
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for combo in combinations(coins, r):
                lcm_val = 1
                for c in combo:
                    lcm_val = math.lcm(lcm_val, c)
                subsets.append((lcm_val, sign))
                
        def count_multiples(m: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (m // lcm_val)
            return total
        
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans