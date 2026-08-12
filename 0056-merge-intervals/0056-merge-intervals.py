class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        start,end=intervals[0][0],intervals[0][1]
        for x in range(1,len(intervals)):
            x=intervals[x]
            if x[0]>end:
                result.append([start,end])
                start,end=x[0],x[1]
            else:
                end=max(end,x[1])
        result.append([start,end])
        return result