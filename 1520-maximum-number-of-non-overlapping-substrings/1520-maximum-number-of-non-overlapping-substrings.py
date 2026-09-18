class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        valid_intervals = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            is_valid = True
            
            i = l
            while i <= r:
                c = s[i]
                if first[c] < l:
                    is_valid = False
                    break
                r = max(r, last[c])
                i += 1
                
            if is_valid:
                valid_intervals.append((l, r))
                
        valid_intervals.sort(key=lambda x: x[1])
        
        result = []
        prev_end = -1
        for l, r in valid_intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r
                
        return result