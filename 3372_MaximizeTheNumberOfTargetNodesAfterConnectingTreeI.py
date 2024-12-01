from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        N1 = len(edges1) + 1
        N2 = len(edges2) + 1
        adj_1 = defaultdict(list)
        adj_2 = defaultdict(list)
        ans = []

        for u, v in edges1:
            adj_1[u].append(v)
            adj_1[v].append(u)

        for u, v in edges2:
            adj_2[u].append(v)
            adj_2[v].append(u)


        def bfs(N, adj, max_level):
            cnt_list = [0] * N

            if max_level < 0:
                return cnt_list

            for root in range(N):
                q = deque()
                q.append(root)
                visit = [False] * N
                level = 0
                cnt = 0
                visit[root] = True

                while q:
                    cur_cnt = len(q)
                    cnt += cur_cnt
                    
                    for i in range(cur_cnt):
                        cur_node = q.popleft()
                        
                        for next_node in adj[cur_node]:
                            if visit[next_node] == False:
                                q.append(next_node)
                                visit[next_node] = True
                    level += 1
                    if level > max_level:
                        break
                cnt_list[root] = cnt

            return cnt_list
        cnt_list2 = bfs(N2, adj_2, k-1)
        cnt_list1 = bfs(N1, adj_1, k)
        
        max_2 = max(cnt_list2)

        for cnt in cnt_list1:
            ans.append(cnt + max_2)
        
        return ans
    

print(Solution().maxTargetNodes([[0,1]], [[0,1]], 0))
print(Solution().maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2))