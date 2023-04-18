class Solution:
    def mostSimilar(self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]) -> list[str]:

        dp = [[len(targetPath)+1 for _ in range(n)] for _ in range(len(targetPath))]
        p = [[None for _ in range(n)] for _ in range(len(targetPath))]

        for i in range(n):
            dp[0][i] = (names[i] != targetPath[0])

        for i in range(1, len(targetPath)):
            for road in roads:
                for j in range(2):
                    u = road[j]
                    v = road[j ^ 1]
                    cur = dp[i-1][u] + (names[v] != targetPath[i])
                    if cur < dp[i][v]:
                        dp[i][v] = cur
                        p[i][v] = u

        v = dp[-1].index(min(dp[-1]))
        ans = [v]
        for i in range(len(targetPath)-1, 0, -1):
            v = p[i][v]
            ans.append(v)
        return reversed(ans)
        