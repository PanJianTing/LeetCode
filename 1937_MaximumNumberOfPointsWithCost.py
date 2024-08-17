from functools import cache 

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        ROW = len(points)
        COL = len(points[0])
        ans = 0

        @cache
        def dp(cur_r, cur_c):
            if cur_r == ROW:
                return 0
            
            res = 0
            for i in range(COL):
                if cur_c == 0:
                    res = max(res, points[cur_r][i] + dp(cur_r+1, i))
                    continue
                res = max(res, points[cur_r][i] - abs(cur_c - i) + dp(cur_r+1, i))
            
            return res
        
        return dp(0,0)
    
    def maxPoints(self, points: list[list[int]]) -> int:
        ROW = len(points)
        COL = len(points[0])
        pre_row = points[0]

        for r in range(1, ROW):
            left_max = [0] * COL
            right_max = [0] * COL
            cur_row = [0] * COL

            left_max[0] = pre_row[0]
            for i in range(1, COL):
                left_max[i] = max(left_max[i-1]-1, pre_row[i])

            right_max[-1] = pre_row[-1]
            for i in range(COL-2, -1, -1):
                right_max[i] = max(right_max[i+1]-1, pre_row[i])

            for i in range(COL):
                cur_row[i] = points[r][i] + max(left_max[i], right_max[i])
            
            pre_row = cur_row
        return max(pre_row)
    
print(Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
print(Solution().maxPoints([[1,5],[2,3],[4,2]]))