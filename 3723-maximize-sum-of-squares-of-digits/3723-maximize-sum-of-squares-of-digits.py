class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9<sum:
            return ""
        res=""
        for x in range(num):
            if sum>9:
                res+="9"
                sum-=9
            else:
                res+=str(sum)
                sum=0
                
        return res
