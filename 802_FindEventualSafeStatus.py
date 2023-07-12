from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        N = len(graph)
        indegree = [0] * N
        adj = [[] for _ in range(N)]

        for i in range(N):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()

        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        
        safe = [False] * N
        while q:
            node = q.popleft()
            safe[node] = True

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        safeNodes = []
        for i in range(N):
            if safe[i]:
                safeNodes.append(i)
        
        return safeNodes

    
print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))