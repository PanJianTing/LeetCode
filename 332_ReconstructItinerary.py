from collections import defaultdict

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