class UnionFind:
    def __init__(self, n: int) -> None:
        self.component = n
        self.representative = [i for i in range(n+1)]
        self.componentSize = [1] * (n+1)

    def findRepresentative(self, node: int):
        if self.representative[node] == node:
            return node
        self.representative[node] = self.findRepresentative(self.representative[node])
        return self.representative[node]
    
    def perform(self, x: int, y: int):
        x = self.findRepresentative(x)
        y = self.findRepresentative(y)

        if x == y:
            return 0
        if self.componentSize[x] > self.componentSize[y]:
            self.componentSize[x] += self.componentSize[y]
            self.representative[y] = x
        else:
            self.componentSize[y] += self.componentSize[x]
            self.representative[x] = y
        
        self.component -= 1
        return 1

    def isConnected(self):
        return self.component == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        a = UnionFind(n)
        b = UnionFind(n)
        edge_required = 0

        for t, u, v in edges:
            if t == 3:
                edge_required += (a.perform(u, v) | b.perform(u, v))
        
        for t, u, v in edges:
            if t == 1:
                edge_required += a.perform(u, v)
            if t == 2:
                edge_required += b.perform(u, v)
        
        if a.isConnected() & b.isConnected():
            return len(edges) - edge_required
        
        return -1
    

print(Solution().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
