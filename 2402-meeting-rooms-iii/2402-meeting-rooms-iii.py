class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        free=[]
        busy=[]
        for x in range(n):
            heapq.heappush(free,x)

        count = [0] * n

        result=0
        ans=0
        meetings.sort()
        curr_time=0
        for start,end in meetings:
            curr_time=max(curr_time,start)

            if not free:
                curr_time=max(curr_time,busy[0][0])

            while busy and busy[0][0]<=curr_time:
                end_time,idx=heapq.heappop(busy)
                heapq,heappush(free,idx)

            idx=heapq.heappop(free)
            heapq.heappush(busy,[curr_time+(end-start),idx])
            count[idx]+=1
            if result<count[idx]:
                ans=idx
                result=count[idx]
            if result==count[idx]:
                ans=min(ans,idx)

        return ans