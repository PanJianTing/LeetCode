from collections import defaultdict
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        N = len(edges1) + 1
        M = len(edges2) + 1
        cnt_g1 = [0] * N
        cnt_g2 = 0

        adj_map1 = defaultdict(list)
        adj_map2 = defaultdict(list)

        for u, v in edges1:
            adj_map1[u].append(v)
            adj_map1[v].append(u)
        
        for u, v in edges2:
            adj_map2[u].append(v)
            adj_map2[v].append(u)

        def bfs(root, dis, adj):
            q = deque()
            q.append((0,root))
            cnt = 0
            visit = set()
            visit.add(root)

            while q:
                cur_dis, cur_node = q.popleft()
                
                if cur_dis <= dis:
                    cnt += 1
                if cur_dis > dis:
                    continue

                for nei_node in adj[cur_node]:
                    if nei_node not in visit:
                        q.append((cur_dis+1, nei_node))
                        visit.add(nei_node)
            return cnt
                
        for i in range(M):
            cnt_g2 = max(cnt_g2, bfs(i, k-1, adj_map2))

        for i in range(N):
            cnt_g1[i] = bfs(i, k, adj_map1) + cnt_g2
        
        return cnt_g1
    

print(Solution().maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2))