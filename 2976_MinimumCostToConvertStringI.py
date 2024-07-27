from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], change: list[str], cost: list[int]) -> int:
        adj = defaultdict(list)
        shortestMatrix = [[float('inf')] * 26 for _ in range(26)]
        res = 0

        for o, c, w in zip(original, change, cost):
            adj[ord(o)-ord('a')].append((ord(c)-ord('a'), w))

        for i in range(26):
            shortestMatrix[i][i] = 0

        
        def dijkstra(cur):
            hq = []
            heapq.heappush(hq, (cur, 0))

            while hq:
                cur_node, cur_w = heapq.heappop(hq)

                for next_node, next_w in adj[cur_node]:
                    if shortestMatrix[cur][next_node] > cur_w + next_w:
                        shortestMatrix[cur][next_node] = cur_w + next_w
                        heapq.heappush(hq, (next_node, next_w + cur_w))
            return
        
        for i in range(26):
            dijkstra(i)

        for s, t in zip(source, target):

            s = ord(s) - ord('a')
            t = ord(t) - ord('a')
            if shortestMatrix[s][t] == float('inf'):
                return -1
            res += shortestMatrix[s][t]
        
        return res
    

    def minimumCost(self, source: str, target: str, original: list[str], change: list[str], cost: list[int]) -> int:
        res = 0
        min_cost = [[float('inf')] * 26 for _ in range(26)]

        for o, c, w in zip(original, change, cost):
            o = ord(o) - ord('a')
            c = ord(c) - ord('a')

            min_cost[o][c] = min(min_cost[o][c], w)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
        
        for s, t in zip(source, target):
            s = ord(s) - ord('a')
            t = ord(t) - ord('a')
            if s == t:
                continue
            if min_cost[s][t] == float('inf'):
                return -1
            res += min_cost[s][t]
        return res

    
print(Solution().minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))
print(Solution().minimumCost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]))
print(Solution().minimumCost("abcd", "abce", ["a"], ["e"], [10000]))
