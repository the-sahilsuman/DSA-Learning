class UnionFind:
    def __init__(self,size=26):
        self.parent=list(range(size))

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x , y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x!=root_y:
            self.parent[root_y]=root_x
    
    def connection(self,x,y):
        return self.find(x)==self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf=UnionFind()

        def to_idx(ch: str) -> int:
            return ord(ch) - ord("a")

        # for eq in equations:
        #     u = to_idx(eq[0])
        #     v = to_idx(eq[3])
        #     if "==" in eq:
        #         if not uf.connection(u,v):
        #             uf.union(u,v)
        #     else:
        #         if uf.connection(u,v):
        #             return False

        for eq in equations:
            if "==" in eq:
                u = to_idx(eq[0])
                v = to_idx(eq[3])
                uf.union(u, v)

        for eq in equations:
            if "!=" in eq:
                u = to_idx(eq[0])
                v = to_idx(eq[3])
                if uf.connection(u, v):
                    return False

        return True