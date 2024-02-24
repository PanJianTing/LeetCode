from collections import defaultdict
from collections import deque
from functools import cache

class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        adj_map = defaultdict(list)

        for n1, n2 in edges:
            adj_map[n1].append(n2)
            adj_map[n2].append(n1)

        def bfs(root) -> int:
            q = deque()
            visit = set()
            nei = (root, 0)
            q.append((root, 0))
        
            while len(q):
                cur, cur_h = q.popleft()
                visit.add(cur)
                for node in adj_map[cur]:
                    if node not in visit:
                        nei = (node, cur_h+1)
                        q.append((node, (cur_h + 1)))
            return nei
        
        cur_node, _ = bfs(0)
        _, ans = bfs(cur_node)

        return ans
    
    def treeDiameter(self, edges: list[list[int]]) -> int:
        N = len(edges) + 1
        adj_map = defaultdict(set)
        leaves = set()
        
        for v1, v2 in edges:
            adj_map[v1].add(v2)
            adj_map[v2].add(v1)
        
        for v in range(N):
            if len(adj_map[v]) == 1:
                leaves.add(v)

        all_v = N
        layer = 0
        while all_v > 2:
            next_leaves = set()
            all_v -= len(leaves)
            for l in leaves:
                nei = adj_map[l].pop()
                adj_map[nei].remove(l)
                if len(adj_map[nei]) == 1:
                    next_leaves.add(nei)
            leaves = next_leaves
            layer += 1

        return layer * 2 + (0 if all_v == 1 else 1)
    
    def treeDiameter(self, edges: list[list[int]]) -> int:
        self.ans = 0
        self.visit = set()
        adj_map = defaultdict(set)
        

        for v1, v2 in edges:
            adj_map[v1].add(v2)
            adj_map[v2].add(v1)

        @cache
        def dfs(cur):
            if cur == None:
                return 0
            self.visit.add(cur)
            first = 0
            second = 0
            
            for nei in adj_map[cur]:
                if nei not in self.visit:
                    count = 1 + dfs(nei)
                    if count > first:
                        second = first
                        first = count
                    else:
                        second = max(second, count)
            self.ans = max(self.ans, first + second)
            return first
        
        dfs(0)
        return self.ans
                




    

print(Solution().treeDiameter([[0,1],[0,2],[1,3],[0,4],[1,5],[2,6],[1,7]])) # 4
print(Solution().treeDiameter([[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]]))       # 5
print(Solution().treeDiameter([[0,1],[0,2]]))                               # 2
print(Solution().treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))             # 4
print(Solution().treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5],[5,6]]))       # 5