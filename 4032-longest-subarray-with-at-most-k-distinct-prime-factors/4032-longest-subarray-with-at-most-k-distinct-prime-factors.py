class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:

        import math
        def finding_factors(n):
            factors=[]

            if n&1==0:
                factors.append(2)
                while n&1==0:
                    n //= 2

            start=3
            while start<=int(math.isqrt(n)):
                if n%start==0:
                    factors.append(start)
                    while n%start==0:
                        n=n//start
                start+=2

            if n > 2:
                factors.append(n)

            return factors
        # print(finding_factors(15))

        factors={}
        for x in nums:
            if x not in factors:
                factors[x]=finding_factors(x)


        result=0
        freq={}
        start,end=0,0
        while start<=end and end<len(nums):
            # print(start,end,freq)
            if len(freq)<=k:
                for x in factors[nums[end]]:
                    if x not in freq:
                        freq[x]=1
                    else:
                        freq[x]+=1
                if len(freq)<=k:
                    result=max(result,end-start+1)
                end+=1
            else:
                for x in factors[nums[start]]:
                    freq[x]-=1
                    if freq[x]==0:
                        del freq[x]
                start+=1

        return result



