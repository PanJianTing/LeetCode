from collections import deque
from collections import defaultdict

class Solution:
    ans = -1

    def dfs(self, curr:int, edges: dict, visit: set, dist: dict):
        visit.add(curr)
        nei = edges[curr]

        if nei == -1:
            return
        
        if nei not in visit:
            dist[nei] = dist[curr] + 1
            self.dfs(nei, edges, visit, dist)
        else:
            if nei in dist:
                self.ans = max(self.ans, dist[curr] - dist[nei] + 1)

    def longestCycle(self, edges: list[int]) -> int:
        
        self.ans = -1
        visit = set()
        for i in range(0, len(edges)):
            if i in visit:
                continue
            dist = {}
            dist[i] = 0
            self.dfs(i, edges, visit, dist)

        return self.ans
    
    def longestCycle(self, edges: list[int]) -> int:

        indegree = defaultdict(int)
        visit = set()

        for edge in edges:
            if edge != -1:
                indegree[edge] += 1
        print(indegree)

        q = deque()

        for i in range(0, len(edges)):
            if indegree[i] == 0:
                q.append(i)

        while len(q):
            curr = q.popleft()
            visit.add(curr)
            nei = edges[curr]
            if nei != -1:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        ans = -1
        for i in range(0, len(edges)):
            if i not in visit:
                count = 1
                visit.add(i)
                nei = edges[i]
                while nei != i:
                    count += 1
                    nei = edges[nei]
                    visit.add(nei)
                ans = max(ans, count)

        return ans






print(Solution().longestCycle([3,3,4,2,3]))
print(Solution().longestCycle([2,-1,3,1]))