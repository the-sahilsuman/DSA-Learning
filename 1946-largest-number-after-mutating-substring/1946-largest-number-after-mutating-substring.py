class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res=""
        
        i=0
        while i<len(num):
            if int(num[i])<change[int(num[i])]:
                j=i
                while j<len(num):
                    if int(num[j])<=change[int(num[j])]:
                        res+=str(change[int(num[j])])
                        j+=1
                    else:
                        res+=num[j:]
                        return res
                return res        
            else:
                res+=num[i]
            i+=1

        return res

        