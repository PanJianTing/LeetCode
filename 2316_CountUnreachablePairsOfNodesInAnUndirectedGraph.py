from collections import defaultdict
from collections import deque

class Solution:

    # group of node
    def bfs(self, n: int, node: int, adj: dict, visit: set) -> int:
        q = deque()
        q.append(node)
        visit.add(node)
        count = 1

        while len(q):
            curr = q.popleft()
            for node in adj[curr]:
                if node not in visit:
                    visit.add(node)
                    count += 1
                    q.append(node)

        return (n - len(visit)) * count
    
    def dfs(self, curr: int, adj: dict, visit: set) -> int:
        
        if curr not in adj:
            return 1
        visit.add(curr)
        count = 1
        for node in adj[curr]:
            if node not in visit:
                visit.add(node)
                count += self.dfs(node, adj, visit)
        return count


    
    def countPairs(self, n: int, edges: list[list[int]]) -> int:

        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visit = set()
        ans = 0
        remainSize = n

        # for i in range(0, n):
        #     if i not in visit:
        #         ans += self.bfs(n, i, adj, visit)

        for i in range(0, n):
            if i not in visit:
                groupSize = self.dfs(i, adj, visit)
                ans += (remainSize - groupSize) * groupSize
                remainSize -= groupSize
        return ans
        
        

        

class UnionFind:

    parent = []
    level = []

    def __init__(self, size: int) -> None:
        self.parent = []
        self.level = []
        for i in range(0, size):
            self.parent.append(i) 
            self.level.append(0)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        xpar = self.find(x)
        ypar = self.find(y)

        if xpar == ypar:
            return
        elif self.level[xpar] > self.level[ypar]:
            self.parent[ypar] = xpar
        elif self.level[xpar] < self.level[ypar]:
            self.parent[xpar] = ypar
        else:
            self.parent[ypar] = xpar
            self.level[xpar] += 1

class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])

        ans = 0
        remainNode = n
        
        parentPair = defaultdict(int)

        for i in range(0, n):
            parent = uf.find(i)
            parentPair[parent] += 1


        for key in parentPair.keys():
            ans += (remainNode - parentPair[key]) * parentPair[key]
            remainNode -= parentPair[key]

        return ans


