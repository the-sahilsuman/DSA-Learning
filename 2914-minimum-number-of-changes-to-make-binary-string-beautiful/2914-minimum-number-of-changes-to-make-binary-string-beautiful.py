class Solution:
    def minChanges(self, s: str) -> int:
        count=0
        for z in range(0,len(s)-1,2):
            if(s[z]!=s[z+1]):
                count=count+1
        return count  