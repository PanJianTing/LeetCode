from collections import defaultdict
from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        N = len(colors)
        adj_map = defaultdict(list)
        indegree = [0] * N

        for u, v in edges:
            adj_map[u].append(v)
            indegree[v] += 1

        count = [[0] * 26 for _ in range(N)]
        q = deque()

        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        
        ans = 1
        visit_node = 0

        while q:
            cur_node = q.popleft()
            cur_color = ord(colors[cur_node]) - ord('a')
            count[cur_node][cur_color] += 1
            ans = max(ans, count[cur_node][cur_color])
            visit_node += 1

            for nei in adj_map[cur_node]:
                for i in range(26):
                    count[nei][i] = max(count[cur_node][i], count[nei][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return -1 if visit_node < N else ans
    

print(Solution().largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]))