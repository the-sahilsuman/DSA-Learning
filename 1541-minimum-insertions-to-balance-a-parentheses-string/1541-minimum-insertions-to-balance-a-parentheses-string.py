class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        stack=0
        i=0
        while i<len(s):
            if s[i]=="(":
                stack+=1
                i+=1
            else:
                if stack>0:
                    stack-=1
                else:
                    count+=1
                if i==len(s)-1:
                    count+=1
                    break
                if s[i+1]==")":
                    i+=2
                else:
                    count+=1
                    i+=1

        return count+stack*2