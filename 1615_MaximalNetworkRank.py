from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n, roads) -> int:
        adjSet = set()

        adj = [0] * n

        for a, b in roads:
            adj[a] += 1
            adj[b] += 1
            adjSet.add((a,b))
            adjSet.add((b,a))

        print(adj)

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                now = adj[i] + adj[j] - (1 if (i,j) in adjSet else 0)
                ans = max(now, ans)

        return ans
    
    def maximalNetworkRank(self, n, roads):
        adj = defaultdict(set)

        for a, b in roads:
            adj[a].add(b)
            adj[b].add(a)
        
        maxRank = 0
        for i in range(n):
            for j in range(i+1, n):
                cur = len(adj[i]) + len(adj[j]) - (1 if i in adj[j] else 0)

                maxRank = max(cur, maxRank)
        return maxRank
    
print(Solution().maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]))
print(Solution().maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
print(Solution().maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))
        

        
