class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                rows[r] |= (1 << (c - 1))
        
        # Bitmasks for each 4-seat block:
        # 2,3,4,5 -> (1<<1) | (1<<2) | (1<<3) | (1<<4) = 0b000011110 = 30
        # 6,7,8,9 -> (1<<5) | (1<<6) | (1<<7) | (1<<8) = 0b011110000 = 480
        # 4,5,6,7 -> (1<<3) | (1<<4) | (1<<5) | (1<<6) = 0b001111000 = 120
        LEFT, RIGHT, MID = 30, 480, 120
        
        ans = 2 * n
        
        for mask in rows.values():
            left = (mask & LEFT) == 0
            right = (mask & RIGHT) == 0
            mid = (mask & MID) == 0
            
            if left and right:
                continue
            elif left or right or mid:
                ans -= 1
            else:
                ans -= 2
                
        return ans