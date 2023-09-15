from collections import defaultdict
import heapq


#my first wrong solution
class Solution:
    def findItinerary(self, tickets):

        N = len(tickets)
        pathDic = defaultdict(list)
        ans = ["JFK"]


        for f, t in tickets:
            temp = pathDic[f]
            heapq.heappush(temp, t)
            pathDic[f] = temp
        
        def dfs(N, f):
            if N == 0:
                return f
            
            if pathDic[curr]:
                return dfs(N-1, heapq.heappop(pathDic[curr]))
            return ""
        for _ in range(N):
            curr = ans[-1]
            next = heapq.heappop(pathDic[curr])
            ans.append(next)
        
        return ans


print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))





class Solution:
    res = []
    def findItinerary(self, tickets):
        
        N = len(tickets)
        pathDic = defaultdict(list)
        visiteDic = defaultdict(list)
        self.res = ["JFK"]
        
        for f, t in tickets:
            pathDic[f].append(t)

        for key, item in pathDic.items():
            item.sort()
            visiteDic[key] = [False] * len(item)

        
        def backtracking(origin, route):
            if len(route) == N+1:
                self.res = list(route)
                return True

            if len(pathDic[origin]) == 0:
                return False
            
            visitList = visiteDic[origin]

            for i, t in enumerate(pathDic[origin]):
                if visitList[i] == False:
                    visitList[i] = True
                    res = backtracking(t, route + [t])
                    visitList[i] = False
                    if res:
                        return True
            
            return False
        backtracking("JFK", ["JFK"])
        return self.res

print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))