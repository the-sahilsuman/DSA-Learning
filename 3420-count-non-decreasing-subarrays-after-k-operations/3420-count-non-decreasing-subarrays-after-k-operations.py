class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        dq = deque()
        cost = 0
        right = n - 1
        
        for left in range(n - 1, -1, -1):
            
            while dq and nums[dq[0]] <= nums[left]:
                idx = dq.popleft()
                next_idx = dq[0] if dq else right + 1
                
                cost += (nums[left] - nums[idx]) * (next_idx - idx)
                
            dq.appendleft(left)
            
            while cost > k:
                cost -= nums[dq[-1]] - nums[right]
                right -= 1
                
                if right < dq[-1]:
                    dq.pop()
                    
            ans += (right - left + 1)
            
        return ans