from collections import deque


class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def countLand():
            q = deque()
            visit = set()
            res = 0
            
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1 and (i, j) not in visit:
                        res += 1
                        q.append((i, j))
                        visit.add((i, j))

                        while q:
                            cur_r, cur_c = q.popleft()

                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                next_r = cur_r + dr
                                next_c = cur_c + dc

                                if 0 <= next_r < M and 0 <= next_c < N:
                                    if grid[next_r][next_c] == 1 and (next_r, next_c) not in visit:
                                        visit.add((next_r, next_c))
                                        q.append((next_r, next_c))

            return res
        
        if countLand() != 1:
            return 0

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    grid[i][j] = 0
                    if countLand() != 1:
                        return 1
                    grid[i][j] = 1
        return 2
                                

