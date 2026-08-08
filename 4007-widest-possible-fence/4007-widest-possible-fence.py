class Solution: 
    def maximumWidth(self, planks: list[int]) -> int:
        # freq = Counter(planks)
        # ans = 0

        # maxH = max(planks) * 2

        # for H in range(1, maxH + 1):
        #     used = Counter()
        #     width = freq[H]

        #     for x in freq:
        #         y = H - x
        #         if y not in freq:
        #             continue

        #         if x > y:
        #             continue

        #         if x == y:
        #             pairs = (freq[x] - used[x]) // 2
        #             width += pairs
        #             used[x] += pairs * 2
        #         else:
        #             pairs = min(freq[x] - used[x],
        #                         freq[y] - used[y])
        #             width += pairs
        #             used[x] += pairs
        #             used[y] += pairs

        #     ans = max(ans, width)
        # return ans

        n = len(planks)

        freq = Counter(planks)
        ans = max(freq.values())

        pairs = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                pairs[planks[i] + planks[j]].append((i, j))

        for h, edges in pairs.items():
            used = [False] * n
            width = freq[h]

            for u, v in edges:
                if not used[u] and not used[v]:
                    used[u] = used[v] = True
                    width += 1

            ans = max(ans, width)

        return ans