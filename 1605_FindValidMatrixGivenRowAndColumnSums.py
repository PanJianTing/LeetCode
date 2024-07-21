class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        M = len(rowSum)
        N = len(colSum)

        cur_row_sum = [0] * M
        cur_col_sum = [0] * N

        res = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                K = min(rowSum[i] - cur_row_sum[i], colSum[j] - cur_col_sum[j])
                res[i][j] = K
                cur_row_sum[i] += K
                cur_col_sum[j] += K
        
        return res
    
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:

        M = len(rowSum)
        N = len(colSum)

        res = [[0] * N for i in range(M)]

        for i in range(M):
            for j in range(N):

                K = min(rowSum[i], colSum[j])

                rowSum[i] -= K
                colSum[j] -= K
                res[i][j] = K
        return res
    
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        M = len(rowSum)
        N = len(colSum)

        i = 0
        j = 0
        res = [[0] * N for _ in range(M)]

        while i < M and j < N:
            K = min(rowSum[i], colSum[j])

            res[i][j] = K
            rowSum[i] -= K
            colSum[j] -= K

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
                
        return res


# print(Solution().restoreMatrix([3,8], [4, 7]))
print(Solution().restoreMatrix([5,7,10], [8,6,8]))