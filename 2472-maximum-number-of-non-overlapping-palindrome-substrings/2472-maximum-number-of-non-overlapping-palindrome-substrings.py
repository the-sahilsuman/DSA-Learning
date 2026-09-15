class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        last_end = -1

        for i in range(n):
            start_k = i - k + 1
            if start_k > last_end:
                sub = s[start_k : i + 1]
                if sub == sub[::-1]:
                    count += 1
                    last_end = i
                    continue

            start_k1 = i - k
            if start_k1 > last_end:
                sub = s[start_k1 : i + 1]
                if sub == sub[::-1]:
                    count += 1
                    last_end = i

        return count