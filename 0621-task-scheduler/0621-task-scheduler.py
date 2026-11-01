class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq={}
        for x in tasks:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
            
        max_freq=max(freq.values())
        count=list(freq.values()).count(max_freq)
        
        # print(count)

        return max(len(tasks),(max_freq-1)*(n+1)+count)