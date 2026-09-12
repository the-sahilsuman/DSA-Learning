class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        items = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: (x[1], x[0]))
        
        r_ends = [it[1] for it in items]
        
        def add_idx(indices: tuple[int, ...], new_idx: int) -> tuple[int, ...]:
            lst = sorted(indices + (new_idx,))
            return tuple(lst)
        
        prefix_dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(n):
            l, r, w, idx = items[i]
            p = bisect_left(r_ends, l) - 1
            
            for k in range(1, 5):
                best_weight, best_indices = prefix_dp[k][i]
                
                if k == 1:
                    cand_weight = w
                    cand_indices = (idx,)
                else:
                    prev_weight, prev_indices = prefix_dp[k - 1][p + 1] if p >= 0 else (0, ())
                    cand_weight = prev_weight + w
                    cand_indices = add_idx(prev_indices, idx)
                
                if (cand_weight > best_weight) or (cand_weight == best_weight and cand_indices < best_indices):
                    best_weight, best_indices = cand_weight, cand_indices
                    
                prefix_dp[k][i + 1] = (best_weight, best_indices)
                
        return list(prefix_dp[4][n][1])