# class Solution:
#     def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
#         free=set()
#         for x in range(k):
#             free.add(x)

#         busy=[]
#         result=[0]*k

#         for idx,x in enumerate(arrival):
#             while busy and x>=busy[0][0]:
#                 _,server=heapq.heappop(busy)
#                 free.add(server)
            
#             if len(free)==0:
#                 continue

#             y=idx
#             while (y%k) not in free:
#                 y+=1

#             heapq.heappush(busy,[x+load[idx],y%k])
#             result[y%k]+=1
#             free.remove(y%k)

#         res=[]
#         temp=max(result)
#         for idx,x in enumerate(result):
#             if x==temp:
#                 res.append(idx)

#         # print(result)
#         return res


from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # SortedList allows us to do binary search in O(log k) time
        free = SortedList(range(k))
        busy = []  # Min-heap storing (end_time, server_index)
        result = [0] * k

        for i, (arr, l) in enumerate(zip(arrival, load)):
            # 1. Free up servers that are done processing
            while busy and busy[0][0] <= arr:
                _, server = heapq.heappop(busy)
                free.add(server)
            
            # 2. If no servers are free, drop the request
            if not free:
                continue

            # 3. Find the smallest server index >= (i % k)
            target = i % k
            idx = free.bisect_left(target)
            
            # If all free servers have an index < target, wrap around to the first free server
            if idx == len(free):
                idx = 0
                
            server = free[idx]
            
            # 4. Allocate the server and mark it as busy
            free.remove(server)
            heapq.heappush(busy, (arr + l, server))
            result[server] += 1

        # 5. Find the server(s) with the maximum requests
        max_req = max(result)
        return [i for i, req in enumerate(result) if req == max_req]