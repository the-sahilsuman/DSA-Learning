class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        l=0
        for index,x in enumerate(s):
            if x.isdigit():
                l=l*int(x)
            else:
                l+=1
            if l>=k:
                break
        
        for x in range(index,-1,-1):
            k=k%l
            # print(l,k)
            if k==0 and s[x].isalpha():
                return s[x]
            if s[x].isdigit():
                l=l//int(s[x])
            else:
                l-=1
        return ""
            
