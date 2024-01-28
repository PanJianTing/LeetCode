from collections import defaultdict
from functools import cache 

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])

        visit = set()

        # @cache
        def dp(curR, curC) -> int:
            if curR > ROW or curC > COL:
                return 0
            if (curR, curC) in visit:
                return 0
            ans = 0
            # print("========{}, {}".format(curR, curC))
            for i in range(ROW):
                if i + curR > ROW:
                    continue
                for j in range(COL):
                    if j + curC > COL:
                        continue
                    all_sum = 0
                    for curI in range(i, i+curR):
                        for curJ in range(j, j+curC):
                            # print(curI, curJ)
                            all_sum += matrix[curI][curJ]
                    # print("sum => {}".format(all_sum))
                    if all_sum == target:
                        ans += 1
            visit.add((curR, curC))
            return ans + dp(curR+1, curC) + dp(curR, curC+1)
        
        return dp(1,1)
    

    def numSubmatrixSumTarget(self, matrix: list[list[int]], target) -> int:
        ans = 0
        ROW = len(matrix)
        COL = len(matrix[0])
        prefixSum = [[0] * (COL+1) for _ in range(ROW+1)]

        for i in range(1, ROW+1):
            for j in range(1, COL+1):
                prefixSum[i][j] = matrix[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
        
        # print(prefixSum)

        for r1 in range(1, ROW+1):
            for r2 in range(r1, ROW+1):
                h = defaultdict(int)
                h[0] = 1
                print(r1, r2)
                for c in range(1, COL+1):
                    # print("r1: {}, r2: {}, c: {}".format(r1, r2, c))
                    cur_sum = prefixSum[r2][c] - prefixSum[r1-1][c]

                    # print("sum : {}, (r2,c) : ({}, {}), (r1-1, c): ({}, {})".format(cur_sum, r2, c, r1-1, c))

                    ans += h[cur_sum-target]
                    h[cur_sum] += 1
        return ans


    
# print(Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))
print(Solution().numSubmatrixSumTarget([[1,-1],[-1,1]], 0))
# print(Solution().numSubmatrixSumTarget([[904]], 0))
                    
                    
                        


