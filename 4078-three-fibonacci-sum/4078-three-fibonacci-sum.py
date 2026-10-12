class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        n1=0
        n2=1
        n3=n1+n2
        total=n1+n2+n3
        while total<=n:
            if total==n:
                return True
            n1,n2=n2,n3
            n3=n1+n2
            # print(n1,n2,n3)
            total=n1+n2+n3
            
        return False