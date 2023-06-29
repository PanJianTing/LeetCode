from collections import deque, defaultdict

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:

        M = len(grid)
        N = len(grid[0])
        q = deque()
        moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        seen = defaultdict(set)
        keySet = set()
        lockSet = set()
        allKeys = 0
        startR = 0
        startC = 0
        for i in range(M):
            for j in range(N):
                cell = grid[i][j]
                if cell in 'abcdef':
                    allKeys += (1 << (ord(cell) - ord('a')))
                    keySet.add(cell)
                if cell in 'ABCDEF':
                    lockSet.add(cell)
                
                if '@' == cell:
                    startR = i
                    startC = j

        q.append((startR, startC, 0, 0))
        seen[0].add((startR, startC))

        while q:
            curR, curC, keys, dis = q.popleft()

            for dR, dC in moves:
                newR = curR + dR
                newC = curC + dC

                if newR >= 0 and newR < M and newC >= 0 and newC < N:
                    newCell = grid[newR][newC]
                    if '#' == newCell:
                        continue

                    if newCell in keySet:
                        if ((1 << (ord(newCell)- ord('a'))) & keys) != 0:
                            continue
                        
                        newKeys = keys | (1 << (ord(newCell) - ord('a')))

                        if newKeys == allKeys:
                            return dis + 1
                        seen[newKeys].add((newR, newC))
                        q.append((newR, newC, newKeys, dis + 1))
                    
                    if newCell in lockSet and 0 == (keys & (1 << (ord(newCell) - ord('A')))):
                        continue
                    elif (newR, newC) not in seen[keys]:
                        seen[keys].add((newR, newC))
                        q.append((newR, newC, keys, dis+1))

        return -1


    
print(Solution().shortestPathAllKeys(["@Aa"]))
print(Solution().shortestPathAllKeys(["@..aA","..B#.","....b"]))
print(Solution().shortestPathAllKeys(["@.a..","###.#","b.A.B"]))



        