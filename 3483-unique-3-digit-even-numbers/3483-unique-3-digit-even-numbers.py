class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        count = 0
        
        for num in range(100, 1000, 2):
            d1 = num // 100          
            d2 = (num // 10) % 10    
            d3 = num % 10          
            
            needed = Counter([d1, d2, d3])
            
            if all(available[d] >= req for d, req in needed.items()):
                count += 1
                
        return count