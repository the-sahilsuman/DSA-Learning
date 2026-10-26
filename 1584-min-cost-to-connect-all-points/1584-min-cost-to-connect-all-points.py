class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        
        heap=[(0,0)]
        visited=set()
        total_cost=0

        while len(visited)<n:
            cost,node=heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost+=cost

            for x in range(n):
                if x not in visited:
                    dist = (abs(points[node][0] - points[x][0]) + abs(points[node][1] - points[x][1]))

                    heapq.heappush(heap,(dist,x))

        return total_cost