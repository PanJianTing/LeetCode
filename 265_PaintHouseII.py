class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:

        if not costs:
            return 0
        M = len(costs)
        N = len(costs[0])

        for i in range(1, M):
            for j in range(N):
                costs[i][j] = costs[i][j] + min(costs[i-1][:j] + costs[i-1][j+1:])
        return min(costs[-1])