from collections import defaultdict, deque
from functools import cache

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:

        courseMap = defaultdict(list)
        timeMap = defaultdict(int)

        for pre, next in relations:
            courseMap[next].append(pre)
        
        @cache
        def dp(cur):
            if cur in timeMap:
                return cur
            
            ans = 0
            if cur not in courseMap:
                ans = time[cur-1]
            else:
                for nextCur in courseMap[cur]:
                    if nextCur in timeMap:
                        ans = max(ans, timeMap[nextCur])
                    else:
                        ans = max(ans, dp(nextCur))
                ans += time[cur-1]
            return ans
        
        for i in range(n):
            timeMap[i+1] = dp(i+1)

        return max(timeMap.values())
    
    def minimumTime(self, n, relations, time) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        spendTime = [0] * n
        q = deque()

        for st, next in relations:
            graph[st-1].append(next-1)
            indegree[next-1] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                spendTime[i] = time[i]
        
        while q:
            cur = q.popleft()
            
            for node in graph[cur]:
                spendTime[node] = max(spendTime[cur], spendTime[node])
                indegree[node] -= 1

                if indegree[node] == 0:
                    q.append(node)
                    spendTime[node] += time[node]
        
        return max(spendTime)
    
    def minimumTime(self, n, relations, time) -> int:

        graph = defaultdict(list)

        for s, e in relations:
            graph[s-1].append(e-1)
        
        @cache
        def dfs(curr):
            if len(graph[curr]) == 0:
                return time[curr]
            
            ans = 0
            for next in graph[curr]:
                ans = max(ans, dfs(next))
            
            return ans + time[curr]

        max_ans = 0
        for i in range(n):
            max_ans = max(max_ans, dfs(i))

        return max_ans

    
print(Solution().minimumTime(3, [[1,3],[2,3]], [3,2,5]))
print(Solution().minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]))