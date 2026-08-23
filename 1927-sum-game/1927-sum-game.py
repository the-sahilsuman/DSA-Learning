class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left = num[:mid]
        right = num[mid:]
        
        s1 = sum(int(c) for c in left if c != '?')
        s2 = sum(int(c) for c in right if c != '?')
        
        q1 = left.count('?')
        q2 = right.count('?')
        
        return (s1 - s2) * 2 != 9 * (q2 - q1)
        