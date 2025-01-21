class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        N = len(grid[0])
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        ans = first_row_sum

        for i in range(N):
            first_row_sum -= grid[0][i]
            ans = min(ans, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][i]

        return ans

print(Solution().gridGame([[2,5,4],[1,5,1]]))