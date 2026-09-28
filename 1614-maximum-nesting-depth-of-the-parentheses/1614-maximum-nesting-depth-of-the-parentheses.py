class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        res=0
        for ch in s:
            if ch=="(":
                stack.append("(")
                res=max(res,len(stack))
            if ch==")":
                stack.pop()
        return res
            