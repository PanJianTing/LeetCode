from collections import defaultdict

class Solution:
    def remainingMethods(self, N: int, k: int, graph: list[list[int]]) -> list[int]:
        g = defaultdict(list)

        for st, end in graph:
            g[st].append(end)
        
        visit = set([k])
        res = []

        def dfs(cur):
            visit.add(cur)
            for next_node in g[cur]:
                if next_node in visit:
                    continue
                dfs(next_node)
        
        dfs(k)

        for node in range(N):
            if node in visit:
                continue
                
            for next_node in g[node]:
                if next_node in visit:
                    return [i for i in range(N)]
            res.append(node)
        
        return res
    
print(Solution().remainingMethods(4, 1, [[1,2],[0,1],[3,2]]))
print(Solution().remainingMethods(5, 0, [[1,2],[0,2],[0,1],[3,4]]))



        