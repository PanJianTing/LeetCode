from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        lose_map = defaultdict(int)
        ans = []
        cur_weak_cnt = float('inf')
        
        for u, v in edges:
            lose_map[v] += 1
        
        for i in range(n):
            if lose_map[i] == cur_weak_cnt:
                ans.append(i)
            if lose_map[i] < cur_weak_cnt:
                cur_weak_cnt = lose_map[i]
                ans = [i]
        
        return ans[0] if len(ans) == 1 else -1
    
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        indegrees = [0] * n
        zero_count = 0
        ans = 0

        for u, v in edges:
            indegrees[v] += 1
        
        for i in range(n):
            if indegrees[i] == 0:
                zero_count += 1
                ans = i
        
        return ans if zero_count == 1 else -1
    
    def findChampion(self, N: int, edges: list[list[int]]) -> int:
        indegree = [True] * N
        cnt = 0
        ans = 0

        for u, v in edges:
            indegree[v] = False
        
        for i in range(N):
            if indegree[i]:
                cnt += 1
                ans = i
        
        return ans if cnt == 1 else -1
        
    

print(Solution().findChampion(3, [[0,1],[1,2]]))
print(Solution().findChampion(4, [[0,2],[1,3],[1,2]]))
        