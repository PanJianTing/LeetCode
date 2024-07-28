from collections import defaultdict, deque
import heapq

class Solution:
    def secondMinimum(self, N: int, edges: list[list[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        dist1 = [float('inf')] * N
        dist2 = [float('inf')] * N
        freq = [0] * N
        hq = []

        for f, t in edges:
            adj[f-1].append(t-1)
            adj[t-1].append(f-1)

        dist1[0] = 0
        heapq.heappush(hq, (0, 0))

        while hq:
            cur_time, cur_node = heapq.heappop(hq)
            freq[cur_node] += 1

            if cur_node == (N-1) and freq[cur_node] == 2:
                return cur_time
            
            next_time = cur_time + time
            if (cur_time // change) & 1:
                next_time = change * (cur_time // change + 1) + time
            
            for next_node in adj[cur_node]:
                if dist1[next_node] > next_time:
                    dist2[next_node] = dist1[next_node]
                    dist1[next_node] = next_time
                    heapq.heappush(hq, (next_time, next_node))
                elif dist2[next_node] > next_time and dist1[next_node] != next_time:
                    dist2[next_node] = next_time
                    heapq.heappush(hq, (next_time, next_node))
        
        return 0
    

    def secondMinimum(self, N: int, edges: list[list[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        dist1 = [-1] * N
        dist2 = [-1] * N
        q = deque()

        for f, t in edges:
            f -= 1
            t -= 1
            adj[f].append(t)
            adj[t].append(f)

        dist1[0] = 0
        q.append((0, 1))

        while q:
            cur_node, cur_freq = q.popleft()
            cur_time = dist1[cur_node] if cur_freq == 1 else dist2[cur_node]

            next_time = cur_time + time
            if (cur_time // change) & 1:
                next_time = change * (cur_time // change + 1) + time
            
            for next_node in adj[cur_node]:
                if dist1[next_node] == -1:
                    dist1[next_node] = next_time
                    q.append((next_node, 1))
                elif dist1[next_node] != next_time and dist2[next_node] == -1:
                    if next_node == N-1:
                        return next_time
                    dist2[next_node] = next_time
                    q.append((next_node, 2))

        return 0
                

            
        
        

    
print(Solution().secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5))
print(Solution().secondMinimum(2, [[1,2]], 3, 2))