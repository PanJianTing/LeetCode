from collections import deque
from collections import defaultdict
from functools import cache


class Solution:
    # BFS MLE
    def findPaths(self, m, n, maxMove, startRow, startColumn) -> int:

        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        q = deque()
        q.append((startRow, startColumn))

        while q and maxMove > 0:
            curNode = len(q)
            
            for _ in range(curNode):
                curR, curC = q.popleft()
                res = 0
                for dr, dc in dirs:
                    nextR = curR + dr
                    nextC = curC + dc
                    if 0 <= nextR < m and 0 <= nextC < n:
                        q.append((nextR, nextC))
                            
                    else:
                        res += 1
                ans += res
            maxMove -= 1
        return ans
    
    def findPatshs(self, m, n, maxMove, startRow, startColumn) -> int:

        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(curR, curC, move) -> int:
            if 0 <= curR < m and 0 <= curC < n:
                if move > 0:
                    res = 0
                    for dr, dc in dirs:
                        res += dp(curR + dr, curC + dc, move - 1)
            
                    return res
                else:
                    return 0
            else:
                return 1
        
        return dp(startRow, startColumn, maxMove) % MOD

                
    
# print(Solution().findPaths(2,2,2,0,0))
print(Solution().findPaths(1,3,3,0,1))
         