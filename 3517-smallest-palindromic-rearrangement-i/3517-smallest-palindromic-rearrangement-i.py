class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq={}
        all=[]
        for x in s:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
                all.append(x)
        
        # print(freq)
        all.sort()
        res=""
        mid=""
        for ch in all:
            if freq[ch]&1:
                mid=ch
            res+=ch*(freq[ch]//2)

        return res+mid+res[::-1]

