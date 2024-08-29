from collections import defaultdict

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        N = len(stones)
        adj = defaultdict(list)
        visited = [0] * N
        group = 0

        for i in range(N):
            for j in range(i+1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)

        def dfs(cur):
            visited[cur] = 1

            for next_node in adj[cur]:
                if visited[next_node] == 0:
                    dfs(next_node)
        
        for i in range(N):
            if visited[i] == 0:
                dfs(i)
                group += 1
        
        return N - group


    

print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(Solution().removeStones([[0,0]]))
print(Solution().removeStones([[0,1],[1,0]]))