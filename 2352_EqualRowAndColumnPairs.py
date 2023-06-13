from collections import defaultdict
from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        N = len(grid)

        colList = []

        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(grid[j][i])
            colList.append(temp)

        # print(colList)
        ans = 0

        for i, row in enumerate(grid):
            for j, col in enumerate(colList):
                if row == col:
                    ans += 1

        return ans
    
    def equalPairs(self, grid: list[list[int]]) -> int:

        ans = 0
        rowSet = defaultdict(int)
        N = len(grid)

        for row in grid:
            rowSet[tuple(row)] += 1
        
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(grid[j][i])
            ans += rowSet[tuple(temp)]

        return ans
    
    def equalPairs(self, grid: list[list[int]]) -> int:

        ans = 0

        cnt = Counter(tuple(row) for row in grid)

        for col in zip(*grid):
            ans += cnt[col]

        return ans




print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

