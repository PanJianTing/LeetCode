from collections import defaultdict
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        N = len(edges1) + 1
        M = len(edges2) + 1

        adj_map1 = defaultdict(list)
        adj_map2 = defaultdict(list)

        ans = []

        for u, v in edges1:
            adj_map1[u].append(v)
            adj_map1[v].append(u)
        
        for u, v in edges2:
            adj_map2[u].append(v)
            adj_map2[v].append(u)

        def bfs(root, adj, cnt):
            q = deque()
            q.append((0,root))
            color = [-1] * cnt
            color_cnt = [0] * 2


            while q:
                cur_color, cur_node = q.popleft()

                color[cur_node] = cur_color
                color_cnt[cur_color] += 1

                next_color = 0 if cur_color else 1
                
                for nei_node in adj[cur_node]:
                    if color[nei_node] == -1:
                        color[nei_node] = next_color
                        q.append((next_color, nei_node))
            return (color, color_cnt)
        

        g1_color, g1_color_cnt = bfs(0, adj_map1, N)
        _, g2_color_cnt = bfs(0, adj_map2, M)
        max_g2_cnt = max(g2_color_cnt)

        for i in range(N):
            node_color = g1_color[i]
            ans.append(g1_color_cnt[node_color]+max_g2_cnt)
        
        return ans
    

print(Solution().maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2))