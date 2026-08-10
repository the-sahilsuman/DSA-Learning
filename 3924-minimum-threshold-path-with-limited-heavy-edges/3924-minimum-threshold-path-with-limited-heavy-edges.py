class Solution:

    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
    
        
        adj = [[] for _ in range(n)]
        max_weight = 0
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            max_weight = max(max_weight, w)

        def canReachWithThreshold(threshold: int) -> bool:
            
            min_heavy_edges = [float('inf')] * n
            min_heavy_edges[source] = 0
            
           
            pq = [(0, source)]
            
            while pq:
                heavy_count, u = heapq.heappop(pq)
                
                if u == target:
                    return heavy_count <= k
                    
                if heavy_count > min_heavy_edges[u]:
                    continue
                    
                for v, w in adj[u]:
                    
                    is_heavy = 1 if w > threshold else 0
                    new_heavy_count = heavy_count + is_heavy
                    
                    if new_heavy_count < min_heavy_edges[v] and new_heavy_count <= k:
                        min_heavy_edges[v] = new_heavy_count
                        heapq.heappush(pq, (new_heavy_count, v))
                        
            return min_heavy_edges[target] <= k

        
        low, high = 0, max_weight
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if canReachWithThreshold(mid):
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1  

        return ans