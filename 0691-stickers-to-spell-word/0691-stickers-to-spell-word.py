class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        full = (1 << m) - 1

        target_count = [0] * 26
        for ch in target:
            target_count[ord(ch) - ord('a')] += 1

        sticker_counts = []

        for sticker in stickers:
            cnt = [0] * 26

            for ch in sticker:
                idx = ord(ch) - ord('a')
                if target_count[idx] > 0:
                    cnt[idx] += 1

            if any(cnt[i] > 0 for i in range(26)):
                sticker_counts.append(cnt)

        for i in range(26):
            if target_count[i] > 0:
                if not any(sticker[i] > 0 for sticker in sticker_counts):
                    return -1

        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0

        for mask in range(1 << m):
            if dp[mask] == INF:
                continue

            for sticker in sticker_counts:
                new_mask = mask
                cnt = sticker.copy()

                for i in range(m):
                    if (new_mask >> i) & 1:
                        continue

                    idx = ord(target[i]) - ord('a')

                    if cnt[idx] > 0:
                        cnt[idx] -= 1
                        new_mask |= (1 << i)

                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)

        return -1 if dp[full] == INF else dp[full]