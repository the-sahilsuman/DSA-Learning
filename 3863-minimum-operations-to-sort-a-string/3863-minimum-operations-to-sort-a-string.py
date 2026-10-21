class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
    
        # Helper to check if a list of characters is sorted
        def is_sorted(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
        
        chars = list(s)
        
        # 1. Already sorted
        if is_sorted(chars):
            return 0
            
        # 2. Impossible case (Length 2, not sorted)
        if n <= 2:
            return -1
            
        # 3. Check if 1 operation is enough
        # Try sorting prefix of length n-1
        prefix_sorted = sorted(chars[:-1]) + [chars[-1]]
        if is_sorted(prefix_sorted):
            return 1
            
        # Try sorting suffix of length n-1
        suffix_sorted = [chars[0]] + sorted(chars[1:])
        if is_sorted(suffix_sorted):
            return 1
            
        # 4. Check if 2 operations are enough
        # Sequence A: Sort Prefix (n-1) -> then Sort Suffix (n-1)
        seq_a = [prefix_sorted[0]] + sorted(prefix_sorted[1:])
        if is_sorted(seq_a):
            return 2
            
        # Sequence B: Sort Suffix (n-1) -> then Sort Prefix (n-1)
        seq_b = sorted(suffix_sorted[:-1]) + [suffix_sorted[-1]]
        if is_sorted(seq_b):
            return 2
            
        # 5. Otherwise, it will always take exactly 3 operations
        return 3