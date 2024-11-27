from collections import defaultdict, deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        adj_map = defaultdict(list)
        ans = []

        for i in range(n-1):
            adj_map[i].append(i+1)
        
        for u, v in queries:
            adj_map[u].append(v)

            q = deque()
            visit = set()
            visit.add(0)
            q.append((0, 0))

            while q:
                cur_node, cur_move = q.popleft()
                if cur_node == n-1:
                    ans.append(cur_move)
                    break
                

                for next_node in adj_map[cur_node]:
                    if next_node not in visit:
                        visit.add(next_node)
                        q.append((next_node, cur_move + 1))
        return ans
    

    def shortestDistanceAfterQueries(self, N: int, queries: list[list[int]]) -> list[int]:
        adj_map = defaultdict(list)
        ans = []
        dp = [-1] * N

        for i in range(N-1):
            adj_map[i].append(i+1)

        def dfs(cur):
            if cur == N-1:
                return 0
            
            if dp[cur] != -1:
                return dp[cur]
            
            min_dep = N
            for next_node in adj_map[cur]:
                min_dep = min(min_dep, 1 + dfs(next_node))
            dp[cur] = min_dep
            return min_dep

        for u, v in queries:
            adj_map[u].append(v)
            ans.append(dfs(0))
            dp = [-1] * N
        
        return ans
    

    def shortestDistanceAfterQueries(self, N: int, queries: list[list[int]]) -> list[int]:
        adj_map = defaultdict(list)
        ans = []

        def find_min():
            dep = [0] * N

            for i in range(N-2, -1, -1):
                min_dep = N
                for next_node in adj_map[i]:
                    min_dep = min(min_dep, 1 + dep[next_node])

                dep[i] = min_dep
            
            return dep[0]

        for i in range(N-1):
            adj_map[i].append(i+1)
        
        for u, v in queries:
            if len(ans) > 0 and ans[-1] == 1:
                ans.append(1)
                continue
            adj_map[u].append(v)
            ans.append(find_min())
        
        return ans
    


    def shortestDistanceAfterQueries(self, N: int, queries: list[list[int]]) -> list[int]:
        adj_map = defaultdict(list)
        depth = [i for i in range(N)]
        ans = []

        for i in range(N-1):
            adj_map[i].append(i+1)

        def bfs(st_node):
            q = deque()
            q.append(st_node)

            while q:
                cur_node = q.popleft()
                for next_node in adj_map[cur_node]:
                    if depth[next_node] > depth[cur_node] + 1:
                        depth[next_node] = depth[cur_node] + 1
                        q.append(next_node)
        

        for u, v in queries:
            adj_map[u].append(v)

            if depth[v] > depth[u] + 1:
                depth[v] = depth[u]+1
                bfs(v)
            ans.append(depth[-1])

        return ans




    


        



            

        