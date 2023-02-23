from collections import defaultdict
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:

        nowCap = w
        leaveProject = k

        proMap = defaultdict(list)

        for i in range(0, len(capital)):
            cap = capital[i]
            pro = profits[i]

            proMap[pro].append(cap)

        # for key in proMap.keys():
        #     proMap[key] = sorted(proMap[key])

        sortedPro = sorted(proMap.keys())

        while leaveProject > 0:

            for i in range(len(sortedPro)-1, -1, -1):
                pro = sortedPro[i]
                capList = proMap[pro]
                isDo = False

                for j in range(0, len(capList)):
                    cap = capList[j]
                    if cap <= nowCap:
                        isDo = True
                        del capList[j]
                        break
                if isDo:
                    nowCap += pro
                    break
            leaveProject -= 1
        print(nowCap)
        return nowCap
    
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:

        n = len(capital)
        project = list(zip(capital, profits))
        project.sort()
        print(project)

        q = []
        ptr = 0
        for i in range(0, k):
            while ptr < n and project[ptr][0] <= w:
                heapq.heappush(q, -project[ptr][1])
                ptr += 1
            if not q:
                break
            w += -heapq.heappop(q)

        return w



print(Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
print(Solution().findMaximizedCapital(3, 0, [3,2,1], [0,1,2]))
