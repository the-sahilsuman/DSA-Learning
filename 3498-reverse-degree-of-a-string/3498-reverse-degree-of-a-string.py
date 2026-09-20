class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, start=1):
            # Value in reversed alphabet: 'a' -> 26, 'z' -> 1
            char_val = ord('z') - ord(ch) + 1
            total += char_val * i
        return total