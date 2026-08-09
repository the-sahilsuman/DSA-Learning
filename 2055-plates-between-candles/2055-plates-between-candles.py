class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # def check(i,j):
        #     while s[i]!="|":
        #         i+=1
        #     while s[j]!="|":
        #         j-=1
        #     if i<j:
        #         result.append(prefix[j]-prefix[i])
        #     else:
        #         result.append(0)

        n = len(s)
        prefix = [0] * n

        left = [-1] * n

        for x in range(n):
            if s[x] == "*":
                prefix[x] = prefix[x - 1] + 1 if x > 0 else 1
                left[x] = left[x - 1] if x > 0 else -1
            else:
                prefix[x] = prefix[x - 1] if x > 0 else 0
                left[x] = x

        right = [-1] * n

        for x in range(n - 1, -1, -1):
            if s[x] == "*":
                right[x] = right[x + 1] if x + 1 < n else -1
            else:
                right[x] = x

        result = []

        for u, v in queries:
            l = right[u]      
            r = left[v] 

            if l == -1 or r == -1 or l >= r:
                result.append(0)
            else:
                result.append(prefix[r] - prefix[l])

        return result