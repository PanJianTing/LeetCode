from collections import deque
from collections import defaultdict

class Solution:
    flipPath = 0

    def dfs(self, node: int, visit: set, adj: dict):
        if node not in adj:
            return None
        visit.add(node)
        for nei in adj[node]:
            neiNode = nei[0]
            sign = nei[1]
            if neiNode not in visit:
                if sign == 0:
                    self.flipPath += 1
                self.dfs(neiNode, visit, adj)

    def bfs(self, node: int, adj: dict) -> int:
        q = deque()
        visit = set()
        flipPath = 0

        q.append(node)

        while len(q):
            curr = q.popleft()
            visit.add(curr)
            for nei in adj[curr]:
                node = nei[0]
                sign = nei[1]
                if node not in visit:
                    if sign == 0:
                        flipPath += 1
                    q.append(node)
        return flipPath          

    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        adj = defaultdict(list)

        self.flipPath = 0
        visit = set()

        for conn in connections:
            adj[conn[0]].append((conn[1], 0))
            adj[conn[1]].append((conn[0], 1))

        # bfs
        # return self.bfs(0, adj)

        self.dfs(0, visit, adj)
        return self.flipPath
    
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        road = set()
        graph = defaultdict(list)
        for u, v in connections:
            road.add((u,v))
            graph[u].append(v)
            graph[v].append(u)

        def dfs(curr, parent):
            self.flipPath += (parent, curr) in road
            for node in graph[curr]:
                if node == parent:
                    continue
                dfs(node, curr)
        dfs(0, -1)

        return self.flipPath