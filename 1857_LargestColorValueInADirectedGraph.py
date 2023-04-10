from collections import deque
from collections import defaultdict

class Solution:    
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:

        n = len(colors)
        adj = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        count = [[0 for _  in range(26)] for _ in range(n)]
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        ans = 1
        seen = 0
        while len(q):
            curr = q.popleft()
            currColor = colors[curr]
            count[curr][ord(currColor) - ord('a')] += 1
            ans = max(ans, count[curr][ord(currColor) - ord('a')])

            seen += 1

            if len(adj[curr]) == 0:
                continue

            for neighbor in adj[curr]:
                for i in range(26):
                    count[neighbor][i] = max(count[neighbor][i], count[curr][i])

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if seen < n:
            return -1
        
        return ans

            
