from collections import deque

class Solution:

    # sol #1 BFS
    def canCrossBFS(self, R, C, cells, days) -> bool:

        lands = [[0] * C for _ in range(R)]
        q = deque()
        visit = set()

        for i in range(0, days):
            waterR, waterC = cells[i]
            lands[waterR-1][waterC-1] = 1
        
        for i in range(C):
            if lands[0][i]:
                continue
            q.append((0, i))
            visit.add((0, i))

        while q:
            curR, curC = q.popleft()
            if curR == R-1:
                return True

            for dR, dC in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nextR = curR + dR
                nextC = curC + dC

                if 0 <= nextR < R and 0 <= nextC < C and lands[nextR][nextC] == 0 and (nextR, nextC) not in visit:
                    visit.add((nextR, nextC))
                    q.append((nextR, nextC))

        return False
    
    # sol #2 DFS
    def canCross(self, R, C, cells, days) -> bool:
        lands = [[0] * C for _ in range(R)]

        for waterR, waterC in cells[:days]:
            lands[waterR-1][waterC-1] = 1
        
        def dfs(r, c):
            if False == (0 <= r < R and 0 <= c < C and lands[r][c] == 0):
                return False

            if r == R - 1:
                return True
            lands[r][c] = -1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if dfs(r+dr, c+dc):
                    return True        
            
            return False
        
        for i in range(C):
            if lands[0][i] == 0 and dfs(0, i):
                return True
        return False


    def latestDayToCross(self, R, C, cells) -> int:

        l = 1
        r = len(cells)
        
        while l < r:
            # mid = (l+r) >> 1 wrong
            mid = r - ((r-l) >> 1)
            # print("ff l => {} mid => {} r => {}".format(l, mid, r))
            if self.canCross(R, C, cells, mid):
                l = mid
            else:
                r = mid - 1
            
        return l
    
print(Solution().latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]]))
print(Solution().latestDayToCross(2, 2, [[1,1],[1,2],[2,1],[2,2]]))
print(Solution().latestDayToCross(3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))

                    

        