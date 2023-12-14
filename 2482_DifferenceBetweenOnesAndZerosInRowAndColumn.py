class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        M = len(grid)
        N = len(grid[0])
        oneR = [0] * M
        oneC  = [0] * N

        diff = [[(M+N) * -1] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    oneR[i] += 1
                    oneC[j] += 1

        for i in range(M):
            for j in range(N):
                diff[i][j] += ((oneR[i] + oneC[j]) << 1)  

        return diff
    
print(Solution().onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))