from collections import defaultdict, deque

class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        N = len(edges) + 1
        adj_map = defaultdict(list)
        self.res = 0

        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)

        def dfs(node, parent):
            s = 1
            child_set = set()

            for nei in adj_map[node]:
                if nei == parent:
                    continue

                size = dfs(nei, node)
                child_set.add(size)
                s += size
            
            if len(child_set) < 2:
                self.res += 1
            return s
        dfs(0, -1)

        return self.res
    
print(Solution().countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))
print(Solution().countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
print(Solution().countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]))
print(Solution().countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]))

