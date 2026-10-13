class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        temp=0
        dir=True
        while k>0:
            if dir:
                if temp<n-1:
                    temp+=1
                    # k-=1
                else:
                    temp-=1
                    # k-=1
                    dir=False
            else:
                if temp>0:
                    temp-=1
                    # k-=1
                else:
                    temp+=1
                    # k-=1
                    dir=True
            k-=1
            
        return temp