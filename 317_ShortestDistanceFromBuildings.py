from collections import deque

class Solution:

    # TLE
    def shortestDistance(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = float('inf')
        all_nums = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    all_nums += 1

        for r in range(ROW):
            for c in range(COL):
                need_dis = 0
                if grid[r][c] == 0:
                    visit_house = 0
                    q = deque()
                    q.append((r, c, 0))
                    visit = set((r,c))

                    while q:
                        cur_r, cur_c, cur_dis = q.popleft()

                        for dr, dc in dis:
                            next_r = cur_r + dr
                            next_c = cur_c + dc

                            if 0 <= next_r < ROW and 0 <= next_c < COL:

                                if grid[next_r][next_c] == 1 and (next_r, next_c) not in visit:
                                    need_dis += (cur_dis + 1)
                                    visit_house += 1
                                    visit.add((next_r, next_c))

                                if grid[next_r][next_c] == 0 and (next_r, next_c) not in visit:
                                    q.append((next_r, next_c, cur_dis + 1))
                                    visit.add((next_r, next_c))
                    if visit_house == all_nums:
                        res = min(res, need_dis)
        return -1 if res == float('inf') else res
    

    def shortestDistance(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = float('inf')
        all_building = 0
        dis_grid = [[0] * COL for _ in range(ROW)]
        meet_grid = [[0] * COL for _ in range(ROW)]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 or grid[r][c] == 2:
                    if grid[r][c] == 1:
                        all_building += 1

                    dis_grid[r][c] = float('inf')

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    q = deque()
                    q.append((r, c, 0))
                    visit = set((r,c))

                    while q:
                        cur_r, cur_c, cur_dis = q.popleft()

                        for dr, dc in dis:
                            next_r = cur_r + dr
                            next_c = cur_c + dc

                            if 0 <= next_r < ROW and 0 <= next_c < COL:

                                if grid[next_r][next_c] == 0 and (next_r, next_c) not in visit:
                                    q.append((next_r, next_c, cur_dis + 1))
                                    dis_grid[next_r][next_c] += (cur_dis + 1)
                                    meet_grid[next_r][next_c] += 1
                                    visit.add((next_r, next_c))
        print(dis_grid)
        print(meet_grid)

        for r in range(ROW):
            for c in range(COL):
                if meet_grid[r][c] == all_building:
                    res = min(res, dis_grid[r][c])
        return -1 if res == float('inf') else res

print(Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))