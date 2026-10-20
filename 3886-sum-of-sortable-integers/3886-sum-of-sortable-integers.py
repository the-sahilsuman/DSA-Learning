class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Helper function to check if list B is a cyclic shift of list A using KMP
        def is_cyclic_shift(A, B):
            k = len(A)
            if k == 1:
                return A[0] == B[0]
                
            # We look for B in A + A (concatenated)
            search_space = A + A
            
            # Build the Longest Prefix Suffix (LPS) array for B
            lps = [0] * k
            j = 0
            for i in range(1, k):
                while j > 0 and B[i] != B[j]:
                    j = lps[j - 1]
                if B[i] == B[j]:
                    j += 1
                lps[i] = j
                
            # Perform KMP search
            j = 0
            # We only need to check up to length 2k - 1
            for i in range(2 * k - 1):
                while j > 0 and search_space[i] != B[j]:
                    j = lps[j - 1]
                if search_space[i] == B[j]:
                    j += 1
                if j == k:
                    return True
                    
            return False

        ans = 0
        # Iterate over all possible values of k
        for k in range(1, n + 1):
            if n % k == 0:
                valid = True
                # Check each block of size k
                for i in range(n // k):
                    start = i * k
                    end = start + k
                    A_i = nums[start:end]
                    B_i = sorted_nums[start:end]
                    
                    if not is_cyclic_shift(A_i, B_i):
                        valid = False
                        break
                        
                if valid:
                    ans += k
                    
        return ans