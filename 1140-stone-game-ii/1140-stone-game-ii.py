class Solution:
    def soln(self,i,chance,m,piles):
        if (i+2*m)>=len(piles):
            if chance:
                print("bob",sum(piles[i:]))
                return sum(piles[i:])
            else:
                print("alice",sum(piles[i:]))
                return 0
        pick=0
        if chance:
            for x in range(m,(2*m)+1):
                print("Bob",i,x,sum(piles[i:i+x]))
                pick=max(pick,sum(piles[i:i+x])+self.soln(i+x,False,max(x,m),piles))
        else:
            for x in range(m,(2*m)+1):
                print("Alice",i,x,sum(piles[i:i+x]))
                pick=max(pick,self.soln(i+x,True,max(x,m),piles))
                
        return pick

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, M):
            if i >= n:
                return 0

            if (i, M) in dp:
                return dp[(i, M)]

            ans = 0

            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                newM = max(M, X)

                current = suffix[i] - solve(i + X, newM)

                ans = max(ans, current)

            dp[(i, M)] = ans
            return ans

        return solve(0, 1)

        # n = len(piles)

        # def solve(i, M):
        #     if i >= n:
        #         return 0

        #     ans = 0
        #     taken = 0

        #     for X in range(1, 2 * M + 1):

        #         if i + X > n:
        #             break

        #         taken += piles[i + X - 1]

        #         opponent = solve(i + X, max(M, X))

        #         total_remaining = sum(piles[i:])

        #         current = total_remaining - opponent

        #         ans = max(ans, current)

        #     return ans

        # return solve(0, 1)



