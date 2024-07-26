from collections import defaultdict, deque
import heapq

class Solution:
    def findTheCity(self, N: int, edges: list[list[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        res = [0] * N

        for f, t, d in edges:
            adj[f].append((t, d))
            adj[t].append((f, d))
        
        for i in range(N):
            q = []
            heapq.heappush(q, (0, i))
            visit = set()

            while q:
                cur_dis, cur_node = heapq.heappop(q)

                visit.add(cur_node)
                for next_node, next_dis in adj[cur_node]:
                    
                    if (cur_dis + next_dis) > distanceThreshold or next_node in visit:
                        continue

                    heapq.heappush(q, ((next_dis + cur_dis), next_node))
            res[i] = len(visit)-1

        min_val = min(res)

        for i in range(N-1, -1, -1):
            if res[i] == min_val:
                return i
            
        return -1
    
    def findTheCity(self, N: int, edges: list[list[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        shortestPath = [[float('inf')] * N for _ in range(N)]

        for i in range(N):
            shortestPath[i][i] = 0
        
        for f, t, d in edges:
            adj[f].append((t, d))
            adj[t].append((f, d))

        def dijkstra(cur):
            hq = []
            heapq.heappush(hq, (cur, 0))
            shortestPath[cur][cur] = 0

            while hq:
                cur_node, cur_dis = heapq.heappop(hq)
                if cur_dis > shortestPath[cur][cur_node]:
                    continue
                for next_node, next_dis in adj[cur_node]:
                    if shortestPath[cur][next_node] > (cur_dis + next_dis):
                        shortestPath[cur][next_node] = cur_dis + next_dis
                        heapq.heappush(hq, (next_node, cur_dis + next_dis))

        for i in range(N):
            dijkstra(i)
        
        res = -1
        can_reach = N
        for i in range(N):
            temp = 0
            for j in range(N):
                if i != j and shortestPath[i][j] <= distanceThreshold:
                    temp += 1
            if temp <= can_reach:
                res = i
                can_reach = temp

        return res
    

    def findTheCity(self, N: int, edges: list[list[int]], distanceThreshold: int) -> int:
        shortestPath = [[float('inf')] * N for _ in range(N)]

        for i in range(N):
            shortestPath[i][i] = 0

        def bellman(cur):
            shortestPath[cur][cur] = 0

            for i in range(N-1):
                update = False
                for s, t, w in edges:
                    if shortestPath[cur][s] != float('inf') and shortestPath[cur][s] + w < shortestPath[cur][t]:
                        shortestPath[cur][t] = shortestPath[cur][s] + w
                        update = True
                    if shortestPath[cur][t] != float('inf') and shortestPath[cur][t] + w < shortestPath[cur][s]:
                        shortestPath[cur][s] = shortestPath[cur][t] + w
                        update = True
                if update == False:
                    break
            

        for i in range(N):
            bellman(i)
        
        res = -1
        can_reach = N
        for i in range(N):
            temp = 0
            for j in range(N):
                if i != j and shortestPath[i][j] <= distanceThreshold:
                    temp += 1
            if temp <= can_reach:
                res = i
                can_reach = temp

        return res

    
    
print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
print(Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
print(Solution().findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], 20))

                    

