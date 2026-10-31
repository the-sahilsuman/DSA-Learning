class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free=[]
        busy=[]
        for x in range(len(servers)):
            heapq.heappush(free,(servers[x],x))

        curr_time=0
        result=[]
        for l in range(len(tasks)):
            curr_time=max(l,curr_time)

            if not free:
                curr_time=max(curr_time,busy[0][0])

            while busy and busy[0][0]<=curr_time:
                time, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            w, idx = heapq.heappop(free)
            
            heapq.heappush(busy, (curr_time + tasks[l], w, idx))
            result.append(idx)

        return result