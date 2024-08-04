from collections import defaultdict, deque
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, N: int, queries: list[list[int]]) -> list[int]:
        len_q = len(queries)
        adj = defaultdict(list)
        ans = [N-1] * len_q

        for i in range(N-1):
            adj[i].append(i+1)
        
        for idx, (st, end) in enumerate(queries):
            adj[st].append(end)

            hq = []
            heapq.heappush(hq, (0, 0))
            visit = set()

            while hq:
                cur_dis, cur_n = heapq.heappop(hq)

                if cur_n == N-1:
                    ans[idx] = cur_dis
                    break
                visit.add(cur_n)
                    
                for next_n in adj[cur_n]:
                    if next_n not in visit:
                        heapq.heappush(hq, (cur_dis+1, next_n))
        return ans
    

    def shortestDistanceAfterQueries(self, N: int, queries: list[list[int]]) -> list[int]:
        len_q = len(queries)
        adj = defaultdict(list)
        ans = [N-1] * len_q

        for i in range(N-1):
            adj[i].append(i+1)
        
        for idx, (st, end) in enumerate(queries):
            adj[st].append(end)

            hq = []
            heapq.heappush(hq, (0, 0))
            distance = [float('inf')] * N
            distance[0] = 0

            while hq:
                cur_dis, cur_n = heapq.heappop(hq)

                if cur_dis > distance[cur_n]:
                    continue

                for next_n in adj[cur_n]:
                    if distance[next_n] > cur_dis+1:
                        distance[next_n] = cur_dis + 1
                        heapq.heappush(hq, (cur_dis+1, next_n))
            ans[idx] = distance[N-1]
        return ans
    
print(Solution().shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))
print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]]))

