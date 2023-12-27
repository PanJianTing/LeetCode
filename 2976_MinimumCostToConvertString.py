from collections import defaultdict
from functools import cache
import heapq

class Solution:
    def minimumCost(self, source, target, original, change, cost) -> int:
        N = len(source)
        adj = defaultdict(list)

        for f, t, c in zip(original, change, cost):
            adj[f].append((c, t))

        @cache
        def bfs(f, t):
            q = []
            visit = set()
            heapq.heappush(q, (0, f))
            
            while q:
                curC, curT = heapq.heappop(q)
                if curT == t:
                    return curC
                visit.add(curT)
                for nextC, nextT in adj[curT]:
                    if nextT not in visit:
                        heapq.heappush(q, (curC + nextC, nextT))

            return -1

        res = 0
        for i in range(N):
            if source[i] == target[i]:
                continue
            min_cost = bfs(source[i], target[i])
            if min_cost == -1:
                return -1
            res += min_cost
        return res
    
print(Solution().minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20])) #28
print(Solution().minimumCost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2])) #12
print(Solution().minimumCost("abcd", "abce", ["a"], ["e"], [10000])) #-1
print(Solution().minimumCost("aaadbdcdac", "cdbabaddba", ["a","c","b","d","b","a","c"], ["c","a","d","b","c","b","d"], [7,2,1,3,6,1,7])) #39