from collections import defaultdict
from collections import deque
import math

# bfs
class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:

        adj = defaultdict(list)
        q = deque()
        ans = 99999999

        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        visit = set()
        visit.add(1)

        q.append(1)

        while len(q):
            node = q.popleft()

            if node not in adj:
                continue
            
            for path in adj[node]:
                ans = min(ans, path[1])
                pathNode = path[0]
                if pathNode not in visit:
                    visit.add(pathNode)
                    q.append(pathNode)

        return ans
    
# dfs
class Solution:
    ans = 9999999
    def dfs(self, node: int, adj: dict, visit: set):

        if node not in adj:
            return
        for path in adj[node]:
            self.ans = min(self.ans, path[1])
            pathNode = path[0]
            if pathNode not in visit:
                visit.add(pathNode)
                self.dfs(pathNode, adj, visit)
        

    def minScore(self, n: int, roads: list[list[int]]) -> int:

        adj = defaultdict(list)
        self.ans = 999999
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        visit = set()
        self.dfs(1, adj, visit)

        return self.ans
    

class UnionFind:
    parent = []
    rank = []

    def __init__(self, size: int) -> None:
        self.parent = []
        self.rank = []
        for i in range(0, size):
            self.parent.append(i)
            self.rank.append(0)
        

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union_set(self, x: int, y: int):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:

    def minScore(self, n: int, roads: list[list[int]]) -> int:
        uf = UnionFind(n+1)
        ans = 999999

        for road in roads:
            uf.union_set(road[0], road[1])
        
        for road in roads:
            if uf.find(1) == uf.find(road[0]):
                ans = min(ans, road[2])

        return ans
        