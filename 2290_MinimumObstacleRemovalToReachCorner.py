from collections import deque
import heapq

class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        hq = []
        visit = set()
        visit.add((0, 0))
        heapq.heappush(hq, (0, 0, 0))
        

        while hq:
            cur_remove, cur_r, cur_c = heapq.heappop(hq)
            
            if cur_r == ROW-1 and cur_c == COL-1:

                return cur_remove
            
            for d_row, d_col in dirs:
                next_row = cur_r + d_row
                next_col = cur_c + d_col
                if 0 <= next_row < ROW and 0 <= next_col < COL and (next_row, next_col) not in visit:
                    visit.add((next_row, next_col))
                    heapq.heappush(hq, (cur_remove + (1 if grid[next_row][next_col] else 0), next_row, next_col))

        return -1

    def minimumObstacles(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_obstacle_grid = [[float('inf')] * COL for _ in range(ROW)]

        min_obstacle_grid[0][0] = grid[0][0]
        q = deque()
        q.append((0, 0, 0))

        while q:
            cur_cnt, cur_row, cur_col = q.popleft()

            if cur_row == ROW-1 and cur_col == COL-1:
                return cur_cnt

            for dr, dc in dirs:
                next_row = cur_row + dr
                next_col = cur_col + dc
                if 0 <= next_row < ROW and 0 <= next_col < COL and min_obstacle_grid[next_row][next_col] == float('inf'):
                    min_obstacle_grid[next_row][next_col] = cur_cnt + grid[next_row][next_col]
                    if grid[next_row][next_col]:
                        q.append((cur_cnt+1, next_row, next_col))
                    else:
                        q.appendleft((cur_cnt, next_row, next_col))

        return min_obstacle_grid[ROW-1][COL-1]
    

    def minimumObstacles(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_obstacle_grid = [[True] * COL for _ in range(ROW)]

        min_obstacle_grid[0][0] = False
        q = deque()
        q.append((0, 0, 0))

        while q:
            cur_cnt, cur_row, cur_col = q.popleft()

            if cur_row == ROW-1 and cur_col == COL-1:
                return cur_cnt

            for dr, dc in dirs:
                next_row = cur_row + dr
                next_col = cur_col + dc
                if 0 <= next_row < ROW and 0 <= next_col < COL and min_obstacle_grid[next_row][next_col]:
                    min_obstacle_grid[next_row][next_col] = False
                    if grid[next_row][next_col]:
                        q.append((cur_cnt+1, next_row, next_col))
                    else:
                        q.appendleft((cur_cnt, next_row, next_col))

        return -1
                        


print(Solution().minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
print(Solution().minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))