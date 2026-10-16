class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # MOD=10**9+7
        # result=0
        # for i in range(len(nums)):
        #     freq=set()
        #     for j in range(i,len(nums)):
        #         freq.add(nums[j])
        #         result+=pow(len(freq),2)
        #         result%=MOD
        
        # return result

        MOD = 10**9 + 7
        n = len(nums)
        
        sum_v = [0] * (4 * n)
        sum_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, l, r, val):
            length = r - l + 1
            sum_sq[node] = (sum_sq[node] + 2 * val * sum_v[node] + val * val * length) % MOD
            sum_v[node] = (sum_v[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
            
        def push_down(node, l, r):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0
                
        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            
            push_down(node, l, r)
            mid = (l + r) // 2
            
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
                
            sum_v[node] = (sum_v[2 * node] + sum_v[2 * node + 1]) % MOD
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD

        last_pos = {}
        ans = 0
        
        for i, num in enumerate(nums):
            start = last_pos.get(num, -1) + 1
            
            update(1, 0, n - 1, start, i, 1)
            
            ans = (ans + sum_sq[1]) % MOD
            
            last_pos[num] = i
            
        return ans