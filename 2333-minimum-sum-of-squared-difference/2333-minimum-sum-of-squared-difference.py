class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        if sum(diffs) <= k:
            return 0
            
        M = max(diffs)
        buckets = [0] * (M + 1)
        
        for d in diffs:
            buckets[d] += 1
            
        for d in range(M, 0, -1):
            if buckets[d] > 0:
                reduce_count = min(buckets[d], k)
                
                buckets[d] -= reduce_count
                buckets[d - 1] += reduce_count
                
                k -= reduce_count
                
                if k == 0:
                    break
                    
        res = 0
        for d in range(1, M + 1):
            if buckets[d] > 0:
                res += buckets[d] * (d * d)
                
        return res