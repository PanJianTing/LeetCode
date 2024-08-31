from collections import defaultdict, deque
import heapq

class Solution:
    def modifiedGraphEdges(self, N: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
        INF = int(2e9)

        def dijkstra():
            adj_matrix = [[INF] * N for _ in range(N)]
            min_distance = [INF] * N
            visited = [False] * N

            min_distance[source] = 0

            for u, v, w in edges:
                if w != -1:
                    adj_matrix[u][v] = w
                    adj_matrix[v][u] = w

            for _ in range(N):
                nearest = -1
                for i in range(N):
                    if not visited[i] and (nearest == -1 or min_distance[i] < min_distance[nearest]):
                        nearest = i
                
                visited[nearest] = True

                for v in range(N):
                    min_distance[v] = min(min_distance[v], min_distance[nearest] + adj_matrix[nearest][v])

            return min_distance[destination]
        
        current_dist = dijkstra()

        if current_dist < target:
            return []
        match_target = current_dist == target

        for edge in edges:
            if edge[2] > 0:
                continue

            edge[2] = INF if match_target else 1

            if match_target == False:
                new_distance = dijkstra()

                if new_distance <= target:
                    match_target = True
                    edge[2] += target - new_distance
        return edges if match_target else []
    

    def modifiedGraphEdges(self, N: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
        INF = int(2e9)

        adj = defaultdict(list)

        for u, v, w in edges:
            if w > 0:
                adj[u].append((v, w))
                adj[v].append((u, w))

        def dijkstra():
            hq = []
            min_distance = [INF] * N
            min_distance[source] = 0

            heapq.heappush(hq, (0, source))

            while hq:
                cur_w, cur_node = heapq.heappop(hq)

                for next_node, next_w in adj[cur_node]:
                    if cur_w + next_w < min_distance[next_node]:
                        min_distance[next_node] = cur_w + next_w
                        heapq.heappush(hq, (cur_w + next_w, next_node))

            return min_distance[destination]
        
        current_dist = dijkstra()

        if current_dist < target:
            return []
        
        if current_dist == target:
            for e in edges:
                if e[2] == -1:
                    e[2] = INF
            return edges
        
        for i, (u, v, w) in enumerate(edges):
            if w > 0:
                continue

            edges[i][2] = 1
            adj[u].append((v, 1))
            adj[v].append((u, 1))

            new_distance = dijkstra()

            if new_distance <= target:
                edges[i][2] += target - new_distance
                
                for j in range(i+1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        
        return []
    

print(Solution().modifiedGraphEdges(5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5))



            
