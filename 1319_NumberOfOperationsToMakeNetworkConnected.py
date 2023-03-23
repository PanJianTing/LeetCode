from collections import deque
from collections import defaultdict

class Solution:
    def bfs(self, curr: int, visit: set, adj: list):
        q = deque()
        q.append(curr)
        visit.add(curr)

        while len(q):
            curr = q.popleft()
            for node in adj[curr]:
                if node not in visit:
                    q.append(node)
                    visit.add(node)

    def dfs(self, curr: int, visit: set, adj: list):
        visit.add(curr)
        for node in adj[curr]:
            if node not in visit:
                self.dfs(node, visit, adj)



    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        needCable = n-1
        if needCable > len(connections):
            return -1
        
        adj = defaultdict(list)

        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])

        visit = set()
        numberOfGroup = 0

        for i in range(0, n):
            if i not in visit:
                numberOfGroup += 1
                self.dfs(i, visit, adj)
        return numberOfGroup - 1
    
class UnionFind:

    parent = []
    level = []
    def __init__(self, size: int) -> None:
        self.parent = []
        self.level = []
        for i in range(0, size):
            self.parent.append(i)
            self.level.append(0)
        pass

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        xparent = self.find(x)
        yparent = self.find(y)

        if xparent == yparent:
            return
        elif self.level[xparent] > self.level[yparent]:
            self.parent[yparent] = xparent
        elif self.level[yparent] > self.level[xparent]:
            self.parent[xparent] = yparent
        else:
            self.parent[yparent] = xparent
            self.level[xparent] += 1

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:

        if len(connections) < n-1:
            return -1

        uf = UnionFind(n)

        for conn in connections:
            uf.union(conn[0], conn[1])

        rootGroup = set()

        for i in range(0, n):
            rootGroup.add(uf.find(i))
        return len(rootGroup) - 1
    
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:

        if len(connections) < n-1:
            return -1

        uf = UnionFind(n)

        rootGroup = n
        for conn in connections:
            if uf.find(conn[0]) != uf.find(conn[1]):
                rootGroup -= 1
                uf.union(conn[0], conn[1])
        return rootGroup - 1
