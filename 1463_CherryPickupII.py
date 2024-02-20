from functools import cache
class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        @cache
        def dp(curR, c1, c2) -> int:
            if curR == ROW:
                return 0
            
            res = 0
            for nextC1 in [c1-1, c1, c1+1]:
                if 0 <= nextC1 < COL:
                    for nextC2 in [c2-1, c2, c2+1]:
                        if 0 <= nextC2 < COL and nextC1 != nextC2:
                            res = max(res, dp(curR+1, nextC1, nextC2))
            
            return grid[curR][c1] + grid[curR][c2] + res
        
        return dp(0, 0, COL-1)
    
    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        
        dp = [[[0] * COL for _ in range(COL)] for _ in range(ROW)]

        for i in range(COL):
            for j in range(COL):
                if i != j:
                    dp[ROW-1][i][j] = grid[ROW-1][i] + grid[ROW-1][j]

        for curR in range(ROW-2, -1, -1):
            for c1 in range(COL):
                for c2 in range(COL):
                    res = 0
                    for nextC1 in [c1-1, c1, c1+1]:
                        if 0 <= nextC1 < COL:
                            for nextC2 in [c2-1, c2, c2+1]:
                                if 0 <= nextC2 < COL and nextC1 != nextC2:
                                    res = max(res, dp[curR+1][nextC1][nextC2])
                    dp[curR][c1][c2] = res + grid[curR][c1] + grid[curR][c2]
        return dp[0][0][COL-1]
    

    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        @cache
        def dp(curR, c1, c2) -> int:
            if curR == ROW:
                return 0
            if c1 < 0 or c1 >= COL or c2 < 0 or c2 >= COL:
                return 0
            
            res = grid[curR][c1]
            if c1 != c2:
                res += grid[curR][c2]

            max_cherry = 0
            for nextC1 in [c1-1, c1, c1+1]:
                for nextC2 in [c2-1, c2, c2+1]:
                    max_cherry = max(max_cherry, dp(curR+1, nextC1, nextC2))
            
            return res + max_cherry
        return dp(0, 0, COL-1)
    

    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        
        dp = [[0] * COL for _ in range(COL)]

        for curR in range(ROW-1, -1, -1):
            next_dp = [[0] * COL for _ in range(COL)]
            for c1 in range(COL):
                for c2 in range(COL):
                    res = 0
                    if c1 == c2:
                        continue

                    if curR != ROW-1:
                        for nextC1 in [c1-1, c1, c1+1]:
                            if 0 <= nextC1 < COL:
                                for nextC2 in [c2-1, c2, c2+1]:
                                    if 0 <= nextC2 < COL and nextC1 != nextC2:
                                        res = max(res, dp[nextC1][nextC2])
                                        
                    next_dp[c1][c2] = res + grid[curR][c1] + grid[curR][c2]
            dp = next_dp
        return dp[0][COL-1]
    

    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        
        if COL == 2:
            return sum(sum(g) for g in grid)
        if COL == 3:
            return sum(sum(g) - min(g) for g in grid)

        dp = [[0] * COL for _ in range(COL)]

        for curR in range(ROW-1, -1, -1):
            next_dp = [[0] * COL for _ in range(COL)]
            for c1 in range(COL):
                for c2 in range(COL):
                    res = 0
                    if c1 == c2:
                        continue

                    if curR != ROW-1:
                        for nextC1 in [c1-1, c1, c1+1]:
                            if 0 <= nextC1 < COL:
                                for nextC2 in [c2-1, c2, c2+1]:
                                    if 0 <= nextC2 < COL and nextC1 != nextC2:
                                        res = max(res, dp[nextC1][nextC2])
                                        
                    next_dp[c1][c2] = res + grid[curR][c1] + grid[curR][c2]
            dp = next_dp
        return dp[0][COL-1]
                

        


print(Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
print(Solution().cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
                
                