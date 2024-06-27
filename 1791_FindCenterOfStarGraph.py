from collections import defaultdict

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        N = len(edges)
        cnt_map = defaultdict(int)

        for u, v in edges:
            cnt_map[u] += 1
            cnt_map[v] += 1

            if cnt_map[u] == N:
                return u
            if cnt_map[v] == N:
                return v
        
        return -1
    
    def findCenter(self, edges: list[list[int]]) -> int:
        N = len(edges)
        cnt_map = defaultdict(int)

        for u, v in edges:
            cnt_map[u] += 1
            cnt_map[v] += 1

            if cnt_map[u] > 1:
                return u
            if cnt_map[v] > 1:
                return v
        
        return -1
    
    def findCenter(self, edges: list[list[int]]) -> int:
        
        return edges[0][0] if (edges[0][0] == edges[1][0]) or (edges[0][0] == edges[1][1]) else edges[0][1]
    

print(Solution().findCenter([[1,2],[2,3],[4,2]]))
print(Solution().findCenter([[1,2],[5,1],[1,3],[1,4]]))