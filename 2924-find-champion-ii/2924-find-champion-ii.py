class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        dp=[0]*n
        for u,v in edges:
            dp[v]+=1
        if dp.count(0)==1:
            return dp.index(0)
        return -1