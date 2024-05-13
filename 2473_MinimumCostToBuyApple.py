from collections import defaultdict
import heapq

class Solution:
    def minCost(self, N: int, roads: list[list[int]], appleCost: list[int], k: int) -> list[int]:
        res = [0] * N

        graph = defaultdict(list)

        for st, end, cost in roads:
            graph[st-1].append((end-1, cost))
            graph[end-1].append((st-1, cost))
        
        def shortestPath(st):
            hq = [(0, st)]
            min_cost = appleCost[st]
            min_path_cost = [float('inf')] * N
            min_path_cost[st] = 0

            while hq:
                cur_cost, cur_node = heapq.heappop(hq)

                min_cost = min(min_cost, appleCost[cur_node] + (k+1) * cur_cost)

                for nei, nei_cost in graph[cur_node]:
                    next_cost = nei_cost + cur_cost
                    if next_cost < min_path_cost[nei]:
                        min_path_cost[nei] = next_cost
                        heapq.heappush(hq, (next_cost, nei))
            
            return min_cost
        
        for i in range(N):
            res[i] = shortestPath(i)
        return res
    

    def minCost(self, N: int, roads: list[list[int]], appleCost: list[int], k: int) -> list[int]:
        graph = defaultdict(list)
        res = list(appleCost)

        for st, end, cost in roads:
            graph[st-1].append((end-1, cost))
            graph[end-1].append((st-1, cost))

        hq = []

        for i in range(N):
            heapq.heappush(hq, (res[i], i))
        

        while hq:
            cur_cost, cur_node = heapq.heappop(hq)

            if res[cur_node] < cur_cost:
                continue
                
            for nei, nei_cost in graph[cur_node]:
                next_cost = res[cur_node] + nei_cost * (k+1)
                if res[nei] > next_cost:
                    res[nei] = next_cost
                    heapq.heappush(hq, (next_cost, nei))
        return res
    
print(Solution().minCost(4, [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], [56,42,102,301], 2))






