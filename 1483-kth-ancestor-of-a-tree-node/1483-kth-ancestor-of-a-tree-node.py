class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG=16
        self.up=[[-1]*self.LOG for _ in range(n)]
        # self.parent=parent

        for i in range(n):
            self.up[i][0] = parent[i]

        for j in range(1, self.LOG):
            for i in range(n):
                ancestor = self.up[i][j - 1]
                if ancestor != -1:
                    self.up[i][j] = self.up[ancestor][j - 1]
        
        
    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if (k >> j) & 1:
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node

        # if k==0 or node==-1:
        #     return node

        # return self.getKthAncestor(self.parent[node],k-1)


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
