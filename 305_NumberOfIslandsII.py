class UnionFind:
    parent = []
    rank = []
    count = 0

    def __init__(self, size: int):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0

    def addLand(self, x: int):
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.count += 1
    
    def isLand(self, x: int) -> bool:
        if self.parent[x] >= 0:
            return True
        return False
    
    def numberOfIslands(self) -> int:
        return self.count
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, land: int, neighbor: int):
        landSet = self.find(land)
        neighborSet = self.find(neighbor)

        if landSet == neighborSet:
            return
        elif self.rank[landSet] < self.rank[neighborSet]:
            self.parent[landSet] = neighborSet
        elif self.rank[landSet] > self.rank[neighborSet]:
            self.parent[neighborSet] = landSet
        else:
            self.parent[neighborSet] = landSet
            self.rank[landSet] += 1
        
        self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        dsu = UnionFind(m * n)
        ans = list()

        for pos in positions:
            landPos = pos[0] * n + pos[1]
            dsu.addLand(landPos)

            for i in range(0, 4):
                neighborX = pos[0] + x[i]
                neighborY = pos[1] + y[i]
                neighborPos = neighborX * n + neighborY

                if neighborX >= 0 and neighborX < m and neighborY >= 0 and neighborY < n and dsu.isLand(neighborPos):
                    dsu.union(landPos, neighborPos)

            ans.append(dsu.numberOfIslands())

        return ans

# Solution().numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]])
Solution().numIslands2(3, 3, [[0,1], [1,2], [2,1], [1,0], [0,2], [0,0], [1,1]])