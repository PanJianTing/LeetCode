from collections import defaultdict, deque
import heapq

class Solution:
    def minimumCost(self, N: int, highways: list[list[int]], discounts: int) -> int:
        
        adj = defaultdict(list)
        dist = [[float('inf')] * (discounts+1) for _ in range(N)]
        visit = set()
        hq = []

        for s, t, cost in highways:
            adj[s].append((t, cost))
            adj[t].append((s, cost))

        hq.append((0, 0, 0))
        dist[0][0] = 0
        
        while hq:
            cur_cost, cur_discount, cur = heapq.heappop(hq)

            visit.add((cur, cur_discount))

            for next_city, next_cost in adj[cur]:
                if cur_cost + next_cost < dist[next_city][cur_discount] and (next_city, cur_discount) not in visit:
                    dist[next_city][cur_discount] = cur_cost + next_cost
                    heapq.heappush(hq, (cur_cost + next_cost, cur_discount, next_city))

                if cur_discount + 1 <= discounts and cur_cost + (next_cost >> 1) < dist[next_city][cur_discount+1] and (next_city, cur_discount + 1) not in visit:
                    dist[next_city][cur_discount+1] = cur_cost + (next_cost >> 1)
                    heapq.heappush(hq, (cur_cost + (next_cost >> 1), cur_discount + 1, next_city))
        

        return -1 if min(dist[N-1]) == float('inf') else min(dist[N-1])
    

    def minimumCost(self, N: int, highways: list[list[int]], discounts: int) -> int:
        
        adj = defaultdict(list)
        dist = [[float('inf')] * (discounts+1) for _ in range(N)]
        hq = []

        for s, t, cost in highways:
            adj[s].append((t, cost))
            adj[t].append((s, cost))

        hq.append((0, 0, 0))
        dist[0][0] = 0
        
        while hq:
            cur_cost, cur_discount, cur = heapq.heappop(hq)

            if cur == N-1:
                return cur_cost

            for next_city, next_cost in adj[cur]:
                if cur_cost + next_cost < dist[next_city][cur_discount]:
                    dist[next_city][cur_discount] = cur_cost + next_cost
                    heapq.heappush(hq, (cur_cost + next_cost, cur_discount, next_city))

                if cur_discount + 1 <= discounts and cur_cost + (next_cost >> 1) < dist[next_city][cur_discount+1]:
                    dist[next_city][cur_discount+1] = cur_cost + (next_cost >> 1)
                    heapq.heappush(hq, (cur_cost + (next_cost >> 1), cur_discount + 1, next_city))
        

        return -1
    
    def minimumCost(self, N: int, highways: list[list[int]], discounts: int) -> int:
        
        adj = defaultdict(list)
        dist = [[float('inf')] * (discounts+1) for _ in range(N)]
        hq = []

        for s, t, cost in highways:
            adj[s].append((t, cost))
            adj[t].append((s, cost))

        hq.append((0, discounts, 0))
        dist[0][discounts] = 0
        
        while hq:
            cur_cost, cur_discount, cur = heapq.heappop(hq)

            if cur == (N-1):
                return cur_cost

            for next_city, next_cost in adj[cur]:
                if cur_cost + next_cost < dist[next_city][cur_discount]:
                    dist[next_city][cur_discount] = cur_cost + next_cost
                    heapq.heappush(hq, (cur_cost + next_cost, cur_discount, next_city))

                if cur_discount - 1 >= 0 and cur_cost + (next_cost >> 1) < dist[next_city][cur_discount-1]:
                    dist[next_city][cur_discount-1] = cur_cost + (next_cost >> 1)
                    heapq.heappush(hq, (cur_cost + (next_cost >> 1), cur_discount - 1, next_city))
        return -1


print(Solution().minimumCost(5, [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], 1)) 
print(Solution().minimumCost(3, [[1,0,4],[2,0,4],[2,1,5]], 1)) 
print(Solution().minimumCost(7, [[1,0,59],[5,3,77],[4,6,28],[2,4,89],[1,4,61],[1,3,25],[1,6,73],[1,2,58],[2,5,2],[6,5,79],[4,3,72],[3,0,9],[2,3,73],[0,6,88],[3,6,36],[5,4,77],[2,6,35],[5,1,30],[0,2,86],[0,4,44],[0,5,81]], 42)) 