# from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s) // 2
        count = Counter(s)

        odd_count = 0
        odd_ch = ""
        for ch, freq in count.items():
            if freq % 2 == 1:
                odd_count += 1
                odd_ch = ch
            count[ch] = freq // 2
        
        if odd_count > 1:
            return ""

        match_len = 0
        while match_len < n and count[target[match_len]] > 0:
            count[target[match_len]] -= 1
            match_len += 1

        if match_len == n:
            cand = target[:n] + odd_ch + target[:n][::-1]
            if cand > target:
                return cand

        for i in range(match_len, -1, -1):
            if i < match_len:
                count[target[i]] += 1
            
            if i == n:
                continue

            target_char = target[i]
            for ch in sorted(count.keys()):
                if ch > target_char and count[ch] > 0:
                    count[ch] -= 1
                    
                    prefix = target[:i] + ch
                    suffix = "".join(sorted(count.elements()))
                    half = prefix + suffix
                    return half + odd_ch + half[::-1]

        return ""