class Solution:
    def minTotalDistance(self, grid) -> int:
        oneList = []
        M = len(grid)
        N = len(grid[0])

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    oneList.append((i,j))

        ans = float('inf')

        for i in range(M):
            for j in range(N):
                path = 0
                for x,y in oneList:
                    dx = abs(x - i)
                    dy = abs(y - j)
                    path += dx+dy
                ans = min(ans, path)

        return ans
    
    def minTotalDistance(self, grid) -> int:
        M = len(grid)
        N = len(grid[0])
        rows = []
        cols = []

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
        
        best_row = rows[len(rows) // 2]
        best_col = sorted(cols)[len(cols) // 2]

        ans = 0
        
        for x in rows:
            ans += abs(x - best_row)
        
        for y in cols:
            ans += abs(y - best_col)
        return ans
    
    def minTotalDistance(self, grid) -> int:
        M = len(grid)
        N = len(grid[0])
        rows = []
        cols = []

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    rows.append(i)

        for j in range(N):
            for i in range(M):
                if grid[i][j]:
                    cols.append(j)
        
        best_row = rows[len(rows) // 2]
        best_col = cols[len(cols) // 2]

        ans = 0

        for x in rows:
            ans += abs(x - best_row)
        
        for y in cols:
            ans += abs(y - best_col)

        return ans
    
print(Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
print(Solution().minTotalDistance([[1,1]]))