from collections import defaultdict, deque

class Solution:
    def canFinish(self, N, pre) -> bool:
        indegree = [0] * N
        adj = defaultdict(list)

        for c1, c2 in pre:
            adj[c2].append(c1)
            indegree[c1] += 1

        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        visit = 0

        while q:
            cur = q.popleft()
            visit += 1

            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return visit == N
    

    def dfs(self, curr, adj, visit, inStack) -> bool:
        if inStack[curr]:
            return True
        
        if visit[curr]:
            return False
        
        visit[curr] = True
        inStack[curr] = True
        
        for nei in adj[curr]:
            if self.dfs(nei, adj, visit, inStack):
                return True
        
        inStack[curr] = False
        return False

    def canFinish(self, N, pre) -> bool:
        adj = defaultdict(list)

        for n1, n2 in pre:
            adj[n2].append(n1)
        
        visit = [False] * N
        inStack = [False] * N

        for i in range(N):
            if self.dfs(i, adj, visit, inStack):
                return False
        
        return True

