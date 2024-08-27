from collections import deque
from collections import defaultdict
import heapq

class Solution:
    # Sol #1 wrong solution (because the visit node can be visit again, but other path have greater prob)
    '''
    n = 4
    edges = [[0,1], [0,2], [1,2], [1,3], [2,3]]
    prob = [0.8, 0.3, 0.8, 1, 1]
    start 0
    end 2
    '''
    def maxProbability(self, n, edges, prob, start, end) -> float:

        ans = 0
        q = deque()
        adj = defaultdict(list)
        visit = set()

        for i, (s, e) in enumerate(edges):
            adj[s].append((e, prob[i]))
            adj[e].append((s, prob[i]))
        
        q.append((start, 1))
        allProb = [0] * n
        allProb[start] = 1.0
        visit.add(start)

        while q:
            curr, currProb = q.popleft()
            visit.add(curr)

            for nextNode, pathProb in adj[curr]:

                nextProb = currProb * pathProb

                if nextNode == end:
                    ans = max(ans, nextProb)
                if nextNode not in visit:
                    q.append((nextNode, nextProb))
        
        return allProb[end]
    
    # Sol #2 Success BFS (Shortest Path Faster Algorithm)
    def maxProbability(self, n, edges, prob, start, end) -> float:

        q = deque()
        adj = defaultdict(list)

        for i, (s, e) in enumerate(edges):
            adj[s].append((e, prob[i]))
            adj[e].append((s, prob[i]))
        
        q.append(start)
        allProb = [0] * n
        allProb[start] = 1.0

        while q:
            curr = q.popleft()

            for nextNode, pathProb in adj[curr]:
                if allProb[curr] * pathProb > allProb[nextNode]:
                    allProb[nextNode] = allProb[curr] * pathProb
                    q.append(nextNode)
        
        return allProb[end]
    
    # Sol #3 Bellman-ford

    def maxProbability(self, n, edges, prob, start, end) -> float:

        maxProb = [0] * n
        maxProb[start] = 1.0

        for i in range(0, n-1):
            update = False
            for idx, (u, v) in enumerate(edges):

                if maxProb[u] * prob[idx] > maxProb[v]:
                    maxProb[v] = maxProb[u] * prob[idx]
                    update = True

                if maxProb[v] * prob[idx] > maxProb[u]:
                    maxProb[u] = maxProb[v] * prob[idx]
                    update = True 
            
            if update == False:
                break

        return maxProb[end]
    
    # Sol #4 Dijkstra's Algorithm
    def maxProbability(self, n, edges, prob, start, end) -> float:

        maxProb = [0] * n
        maxProb[start] = 1.0

        pq = []
        pq.append((-1.0, start))

        adj = defaultdict(list)

        for i, (s, e) in enumerate(edges):
            adj[s].append((e, prob[i]))
            adj[e].append((s, prob[i]))

        while pq:
            currProb, curr = heapq.heappop(pq)
            if curr == end:
                return -currProb

            for next, nextProb in adj[curr]:

                if -currProb * nextProb > maxProb[next]:
                    maxProb[next] = -currProb * nextProb
                    heapq.heappush(pq, (-maxProb[next], next))
        return 0.0


# Solution().maxProbability()
print(Solution().maxProbability(4, [[0,1], [0,2], [1,2], [1,3], [2,3]], [0.8, 0.3, 0.8, 1, 1], 0, 2))
