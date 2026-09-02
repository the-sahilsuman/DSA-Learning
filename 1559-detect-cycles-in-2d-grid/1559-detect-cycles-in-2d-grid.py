class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])

        def check(i,j):

            q=deque()
            q.append((i,j,-1,-1))

            while q:
                u,v,pu,pv=q.popleft()

                for du,dv in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nu=u+du
                    nv=v+dv
                    if 0<=nu<m and 0<=nv<n:
                        if (nu, nv) == (pu, pv):
                            continue
                        if grid[u][v]==grid[nu][nv]:
                            if visited[nu][nv]==1:
                                # print(u,v,nu,nv,pu,pv)
                                return True
                            
                            visited[nu][nv]=1
                            q.append((nu,nv,u,v))

            return False

        visited=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0:
                    # print(visited)
                    visited[i][j]=1
                    if check(i,j):
                        return True
        
        return False


