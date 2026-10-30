class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph=[[] for _ in range(n)]

        for u,v,w in edges:
            graph[u].append([v,w])

        dp=[[float("inf")]*(k+1) for _ in range(n)]

        q=[]
        q.append((0,0,1))

        while q:
            cost,node,count=heapq.heappop(q)
            if node==n-1:
                return cost
            for v,w in graph[node]:
                new_cost=cost+w
                temp=count
                if labels[node]==labels[v]:
                    temp+=1
                else:
                    temp=1
                if temp>k:
                    continue
                if new_cost<dp[v][temp]:
                    heapq.heappush(q,(new_cost,v,temp))
                    dp[v][temp]=new_cost
            
        return -1
            
        
        
        
        # def check(s):
        #     n=len(s)
        #     arr=[1]*n
        #     for x in range(1,n):
        #         if s[x]==s[x-1]:
        #             arr[x]=arr[x-1]+1
        #     return max(arr)<=k

        # s=labels
        # graph=[[] for _ in range(n)]

        # for u,v,w in edges:
        #     graph[u].append([v,w])

        # def bfs(i,visited,path):
        #     if i==n-1:
        #         # print(path)
        #         if check(path):
        #             return 0
        #         else:
        #             return float("inf")
            
        #     pick=float("inf")
        #     for v,w in graph[i]:
        #         if v not in visited:
        #             visited.add(v)
        #             pick=min(pick,w+bfs(v,visited,path+s[v]))
        #             visited.remove(v)

        #     return pick
        
        # visited=set()
        # visited.add(0)
        # result=bfs(0,visited,s[0])
        # if result!=float("inf"):
        #     return result
        # return -1
