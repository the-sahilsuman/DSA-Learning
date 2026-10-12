class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        if n < 2:
            return []
            
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
            
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        
        dp = [(float('inf'), []) for _ in range(s + 1)]
        dp[0] = (0, [])  
        
        for p in primes:
            for v in range(s, p - 1, -1):
                if dp[v - p][0] != float('inf'):
                    cand_size = dp[v - p][0] + 1
                    cand_list = dp[v - p][1] + [p]
                    
                    if cand_size < dp[v][0] or (cand_size == dp[v][0] and cand_list < dp[v][1]):
                        dp[v] = (cand_size, cand_list)
                        
        for v in range(s, 0, -1):
            if dp[v][0] != float('inf'):
                return dp[v][1]
                
        return []