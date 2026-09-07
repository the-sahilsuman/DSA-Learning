class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for ch in s:
            new_dp = 2 * dp

            if ch in last:
                new_dp -= last[ch]

            last[ch] = dp
            dp = new_dp % MOD

        return (dp - 1) % MOD




        # result=set()
        # n=len(s)
        # for x in range(1,(1<<n)):
        #     new=""
        #     for i in range(n):
        #         if x & (1 << i):
        #             new += s[i]
                
        #     result.add(new)

        # return len(result)
