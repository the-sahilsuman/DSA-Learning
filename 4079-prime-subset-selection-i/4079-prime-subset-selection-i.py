class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n<2:
            return []

        arr=[True]*(n+1)
        if n>=2:
            arr[0]=arr[1]=False
            
        for i in range(2,int(n**0.5)+1):
            if arr[i]:
                for j in range(i*i,n+1,i):
                    arr[j]=False

        result=[]
        total=0
        for i in range(n+1):
            if arr[i]:
                total+=i
                if total<=s:
                    result.append(i)
                else:
                    break

        return result
                