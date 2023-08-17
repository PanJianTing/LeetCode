from collections import deque

class Solution:
    # Memory Limit Exceed
    def updateMatrix(self, mat):
        R = len(mat)
        C = len(mat[0])

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] #(r, c)

        def bfs(r, c):
            ans = 1
            q = deque()
            q.append((r, c))
            
            while q:
                
                for _ in range(len(q)):
                    curR, curC = q.popleft()
                    for dr, dc in dir:
                        nextR = curR + dr
                        nextC = curC + dc
                        if 0 <= nextR < R and 0 <= nextC < C:

                            if mat[nextR][nextC] == 0:
                                return ans
                            else:
                                q.append((nextR, nextC))
                
                ans += 1

            return ans
        res = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1:
                    res[i][j] = bfs(i, j)

        return res
    
    # bfs according 0
    def updateMatrix(self, mat):
        R = len(mat)
        C = len(mat[0])
        visit = set()
        q = deque()

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] #(r, c)
        res = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0 and (i, j) not in visit:
                    q.append((i, j))
                    visit.add((i, j))
        level = 0
        while q:

            for _ in range(len(q)):
                curR, curC = q.popleft()
                res[curR][curC] = level
                for dr, dc in dir:
                    nextR = curR + dr
                    nextC = curC + dc
                    if 0 <= nextR < R and 0 <= nextC < C and (nextR, nextC) not in visit:
                        q.append((nextR, nextC))
                        visit.add((nextR, nextC))
            
            level += 1
        
        return res
    
    def updateMatrix(self, mat):
        R = len(mat)
        C = len(mat[0])

        dp = [[0] * C for _ in range(R)]
        if mat[0][0] == 1:
            dp[0][0] = 99999999

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1:
                    if i - 1 < 0 and j - 1 < 0:
                        continue
                    if i-1 < 0:
                        dp[i][j] = 1 + dp[i][j-1]
                    elif j - 1 < 0:
                        dp[i][j] = 1 + dp[i-1][j]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                if mat[i][j] == 1:
                    if i+1 >= R and j+1 >= C:
                        continue

                    if i + 1 >= R:
                        dp[i][j] = min(dp[i][j], 1 + dp[i][j+1])
                    elif j + 1 >= C:
                        dp[i][j] = min(dp[i][j], 1 + dp[i+1][j])
                    else:
                        dp[i][j] = min(dp[i][j], 1 + min(dp[i+1][j], dp[i][j+1]))

        return dp
    
    def updateMatrix(self, mat):
        R = len(mat)
        C = len(mat[0])
        dp = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    continue

                minVal = 999999999

                if r > 0:
                    minVal = min(minVal, dp[r-1][c])
                if c > 0:
                    minVal = min(minVal, dp[r][c-1])
                
                dp[r][c] = 1 + minVal
        
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if mat[r][c] == 0:
                    continue

                minVal = 999999999

                if r + 1 < R:
                    minVal = min(minVal, dp[r+1][c])
                if c + 1 < C:
                    minVal = min(minVal, dp[r][c+1])
                
                dp[r][c] = min(dp[r][c], 1 + minVal)
        
        return dp
                




print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(Solution().updateMatrix([[1,1,1],[1,1,1],[0,0,0]]))
print(Solution().updateMatrix([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]))