class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        res = 0

        for x1 in range(M):
            for y1 in range(N):
                for x2 in range(x1, M):
                    for y2 in range(y1, N):
                        allOne = True
                        for x in range(x1, x2+1):
                            for y in range(y1, y2+1):
                                if matrix[x][y] == '0':
                                    allOne = False
                        if allOne:
                            res = max(res, (x2 - x1 + 1) * (y2 - y1 + 1))
        return res
    

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        dp = [[0] * N for _ in range(M)]
        res = 0

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 if j == 0 else dp[i][j-1] + 1
                
                cur_w = dp[i][j]
                cur_h = 1
                for k in range(i, -1, -1):
                    res = max(res, cur_h * min(cur_w, dp[k][j]))
                    cur_h += 1
        
        return res
    
print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

        