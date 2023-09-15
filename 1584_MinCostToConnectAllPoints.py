from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        N = len(points)
        visit = set()
        adj = defaultdict(list)

        def distance(x: list[int], y: list[int]):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        for i in range(N):
            curP = points[i]
            for j in range(N):
                if i == j:
                    adj[i].append(999999999)
                else:
                    adj[i].append(distance(curP, points[j]))
        
        ans = 0
        for i in range(N):
            curDis = adj[i]
            curMinDis = curDis[0]
            curMinIdx = 0
            for j in range(1, len(curDis)):
                if curMinDis > curDis[j]:
                    curMinDis = curDis[j]
                    curMinIdx = j
            
            if (i, curMinIdx) not in visit and (curMinIdx, i) not in visit:
                visit.add((i, curMinIdx))
                ans += curMinDis

        return 0 if N == 1 else ans
    

    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        N = len(points)
        inMST = [False] * N
        hq = [(0, 0)]
        cost = 0
        path = 0

        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        while path < N:
            curW, curNode = heapq.heappop(hq)

            if inMST[curNode]:
                continue

            cost += curW
            inMST[curNode] = True
            path += 1
            for i in range(0, N):
                if inMST[i] == False:
                    heapq.heappush(hq, (distance(points[curNode], points[i]), i))
            
        return cost
            


print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(Solution().minCostConnectPoints([[0,0]]))
print(Solution().minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))
