class Solution:
    def digitSum(self, s: str, k: int) -> str:
        

        def digit_count(x):
            total=0
            while x>0:
                total+=(x%10)
                x//=10
            return total

        result=""
        n=len(s)
        if n<=k:
            return s
        i=0
        while i<n:
            if (i+k)<n:
                temp=s[i:i+k]
            else:
                temp=s[i:]
            result+=str(digit_count(int(temp)))
            i=i+k
        print(result)

        if len(result)>k:
            return self.digitSum(result,k)
        return result
