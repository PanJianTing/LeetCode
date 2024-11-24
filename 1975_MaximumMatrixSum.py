class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        min_val = float('inf')
        negative_cnt = 0
        ans = 0

        for i in range(ROW):
            for j in range(COL):
                min_val = min(min_val, abs(matrix[i][j]))
                ans += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negative_cnt += 1

        if negative_cnt & 1:
            ans -= (min_val << 1)

        return ans

        
print(Solution().maxMatrixSum([[1,-1],[-1,1]]))
print(Solution().maxMatrixSum([[1,-1],[-1,1]]))