from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:

        def topoSort(edges, N):
            adj = defaultdict(list)
            visit = [0] * (N+1)
            order_list = []

            for a, b in edges:
                adj[a].append(b)

            for node in range(1, N+1):
                if visit[node] == 0:
                    has_cycle = dfs(node, adj, visit, order_list)
                    if has_cycle:
                        return []
            
            return order_list[::-1]
        
        def dfs(cur, adj, visit, order):
            visit[cur] = 1
            for next_node in adj[cur]:
                if visit[next_node] == 0:
                    has_cycle = dfs(next_node, adj, visit, order)
                    if has_cycle:
                        return True
                elif visit[next_node] == 1:
                    return True
            visit[cur] = 2
            order.append(cur)
            return False
        
        order_rows = topoSort(rowConditions, k)
        order_cols = topoSort(colConditions, k)

        if order_rows == [] or order_cols == []:
            return []
        
        res = [[0] * k for _ in range(k)]

        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_cols[j]:
                    res[i][j] = order_cols[j]
        return res
    

    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:

        def topo_sort(edge, N):
            deg = [0] * (N+1)
            order = []
            adj = defaultdict(list)
            q = deque()

            for a, b in edge:
                adj[a].append(b)
                deg[b] += 1
            
            for node in range(1, N+1):
                if deg[node] == 0:
                    q.append(node)

            while q:
                cur_node = q.popleft()
                order.append(cur_node)

                for next_node in adj[cur_node]:
                    deg[next_node] -= 1
                    if deg[next_node] == 0:
                        q.append(next_node)
            
            for d in deg:
                if d != 0:
                    return []

            return order
        
        row_order = topo_sort(rowConditions, k)
        col_order = topo_sort(colConditions, k)
        res = [[0] * k for _ in range(k)]

        if row_order == [] or col_order == []:
            return []
        
        for i in range(k):
            for j in range(k):
                if row_order[i] == col_order[j]:
                    res[i][j] = row_order[i]
        return res


print(Solution().buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))
            