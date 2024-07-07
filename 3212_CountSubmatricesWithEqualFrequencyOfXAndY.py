from collections import defaultdict
import heapq

class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0

        dp = [[[0] * 2 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                temp = [0,0]
                left = [0,0]
                top = [0,0]
                leftTop = [0,0]

                if 0 <= i-1:
                    top = dp[i-1][j]
                if 0 <= j-1:
                    left = dp[i][j-1]
                if 0 <= i-1 and 0 <= j-1:
                    leftTop = dp[i-1][j-1]

                temp[0] = (grid[i][j] == 'X') + left[0] + top[0] - leftTop[0]
                temp[1] = (grid[i][j] == 'Y') + left[1] + top[1] - leftTop[1]
                if (temp[0] == temp[1]) and temp[0] > 0:
                    res += 1
                dp[i][j] = temp
        return res
    
print(Solution().numberOfSubmatrices([["X","Y","."],["Y",".","."]]))        
print(Solution().numberOfSubmatrices([["X","X"],["X","Y"]]))        
print(Solution().numberOfSubmatrices([[".","."],[".","."]]))        

            
