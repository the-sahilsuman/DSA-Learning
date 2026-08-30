class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod=(10**9)+7
        result=0
        for num in nums:
            w=num%10
            d=num//10
            s_d=str(d)
            x=int(s_d[:w]) if w > 0 else 0
            y=int(s_d[w:]) if w < len(s_d) else 0
            result = (result + pow(x, y, mod)) % mod
        return result