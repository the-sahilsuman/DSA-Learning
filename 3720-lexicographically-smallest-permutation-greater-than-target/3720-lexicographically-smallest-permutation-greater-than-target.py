class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        if len(target) != n:
            return ""

        count = Counter(s)
        match_len = 0
        while match_len < n and count[target[match_len]] > 0:
            count[target[match_len]] -= 1
            match_len += 1

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
                    return prefix + suffix

        return ""