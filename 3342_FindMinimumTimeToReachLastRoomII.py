import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        ROW = len(moveTime)
        COL = len(moveTime[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        hq = []
        heapq.heappush(hq, (0, 0, 0, 1))
        visit.add((0, 0))

        while hq:
            cur_t, cur_r, cur_c, cur_move_time = heapq.heappop(hq)

            if cur_r == ROW - 1 and cur_c == COL - 1:
                return cur_t
            next_move_time = 2 if cur_move_time == 1 else 1
            for dr, dc in dirs:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if 0 <= next_r < ROW and 0 <= next_c < COL:
                    if (next_r, next_c) not in visit:
                        next_t = max(cur_t, moveTime[next_r][next_c]) + cur_move_time
                        visit.add((next_r, next_c))
                        heapq.heappush(hq, (next_t, next_r, next_c, next_move_time))

        return -1

                


print(Solution().minTimeToReach([[56,93],[3,38]]))
print(Solution().minTimeToReach([[0,0,0],[0,0,0]]))
print(Solution().minTimeToReach([[15,58],[67,4]]))
print(Solution().minTimeToReach([[31,52],[47,94]]))
        