class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result=defaultdict(set)
        n=len(s)

        def backtracking(idx,score,temp,count):
            if score<0:
                return
            if idx==n:
                if score==0:
                    result[count].add(temp)
                return

            if s[idx]=="(":
                backtracking(idx+1,score+1,temp+s[idx],count)
                backtracking(idx+1,score,temp,count+1)

            elif s[idx]==")":
                backtracking(idx+1,score-1,temp+s[idx],count)
                backtracking(idx+1,score,temp,count+1)

            else:
                backtracking(idx+1,score,temp+s[idx],count)
            

        backtracking(0,0,"",0)
        print(result)
        return list(result[min(result.keys())])
            
