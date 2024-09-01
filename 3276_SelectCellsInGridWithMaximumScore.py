from collections import defaultdict, deque
import heapq

class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])

        def dp(cur_r, cur_set):
            if cur_r == ROW:
                return 0

            res = dp(cur_r+1, cur_set)
            for cur_c in range(COL):
                if grid[cur_r][cur_c] not in cur_set:
                    cur_set.add(grid[cur_r][cur_c])
                    res = max(res, grid[cur_r][cur_c] + dp(cur_r+1, cur_set))
                    cur_set.remove(grid[cur_r][cur_c])
            return res

        return dp(0, set())
    
    def maxScore(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        value_set = set([grid[i][j] for i in range(ROW) for j in range(COL)])

        value_list = sorted(list(value_set), reverse = True)

        val_to_rows = defaultdict(list)

        for val in value_list:
            val_to_rows[val] = [r for r in range(ROW) if val in grid[r]]

        def bfs(row_set, remaining_values, score):
            if remaining_values == []:
                return score
            
            value = remaining_values[0]
            remaining_values = remaining_values[1:]

            score_list = []

            for row in val_to_rows[value]:
                if row not in row_set:
                    score_list.append(bfs(row_set | {row}, remaining_values, score + value))
            if not score_list:
                score_list.append(bfs(row_set, remaining_values, score))
            return max(score_list)
        return bfs(set(), value_list, 0)
    
print(Solution().maxScore([[1,2,3],[4,3,2],[1,1,1]]))
print(Solution().maxScore([[8,7,6],[8,3,2]]))
print(Solution().maxScore([[5,5],[5,5],[11,5]]))


                              