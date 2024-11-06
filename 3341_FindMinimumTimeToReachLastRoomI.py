import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        M = len(moveTime)
        N = len(moveTime[0])

        hq = []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * N for _ in range(M)]
        heapq.heappush(hq, [0, 0, 0])
        visited[0][0] = True

        while hq:
            cost, cur_i, cur_j = heapq.heappop(hq)

            if cur_i == M-1 and cur_j == N-1:
                return cost
            
            for di, dj in dirs:
                next_i = di + cur_i
                next_j = dj + cur_j

                if 0 <= next_i < M and 0 <= next_j < N and visited[next_i][next_j] == False:
                    visited[next_i][next_j] = True
                    heapq.heappush(hq, [max(cost + 1, moveTime[next_i][next_j] + 1), next_i, next_j])
        
        return -1

                


print(Solution().minTimeToReach([[56,93],[3,38]]))
print(Solution().minTimeToReach([[0,0,0],[0,0,0]]))
print(Solution().minTimeToReach([[15,58],[67,4]]))
print(Solution().minTimeToReach([[31,52],[47,94]]))
        