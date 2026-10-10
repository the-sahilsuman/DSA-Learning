class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        def countAtLeast(lim: int) -> int:
            freq = {}
            ans = 0
            start = 0
            valid_k = 0  # Tracks how many distinct elements have frequency >= m
            
            for end in range(len(nums)):
                # 1. Expand the window by adding the end element
                freq[nums[end]] = freq.get(nums[end], 0) + 1
                if freq[nums[end]] == m:
                    valid_k += 1
                
                # 2. Shrink the window as long as it satisfies our conditions
                while len(freq) >= lim and valid_k >= k:
                    left_val = nums[start]
                    freq[left_val] -= 1
                    
                    if freq[left_val] == m - 1:
                        valid_k -= 1
                    if freq[left_val] == 0:
                        del freq[left_val]
                        
                    start += 1
                
                # 3. Add the number of valid left endpoints for the current 'end'
                ans += start
                
            return ans

        # Exactly K distinct = (At least K) - (At least K + 1)
        return countAtLeast(k) - countAtLeast(k + 1)




        # n=len(nums)
        # freq={}
        
        # count=0
        # start=0
        # end=0
        # while start<=end and end<n:
        #     if nums[end] in freq:
        #         freq[nums[end]]+=1
        #     else:
        #         freq[nums[end]]=1

        #     # print(freq)

        #     if len(freq)<k:
        #         end+=1
        #     elif len(freq)==k:
        #         if min(freq.values())>=m:
        #             count+=1
        #         end+=1
        #     else:
        #         freq[nums[start]]-=1
        #         freq[nums[end]]-=1
        #         if freq[nums[start]]==0:
        #             del freq[nums[start]]
        #         start+=1
                

        # return count