class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        start,end=0,0
        result=0
        while end<len(s) and start<=end:
            while end<len(s):
                if s[end] in freq:
                    if freq[s[end]]<2:
                        freq[s[end]]+=1
                    else:
                        # print(start,end)
                        break
                else:
                    freq[s[end]]=1
                end+=1
            result=max(result,end-start)
            freq[s[start]]-=1
            start+=1

        return result
