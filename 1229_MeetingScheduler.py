import heapq

class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        M = len(slots1)
        N = len(slots2)

        slots1.sort()
        slots2.sort()
        j = 0
        
        for i in range(M):
            while j < N and slots2[j][0] <= slots1[i][1]:
                st = max(slots2[j][0], slots1[i][0])
                end = min(slots2[j][1], slots1[i][1])
                if end - st >= duration:
                    return [st, st+duration]
                if slots2[j][1] > slots1[i][1]:
                    break
                j += 1
        return []
    
    def minAvailableDuration(self, s1: list[list[int]], s2: list[list[int]], d: int) -> list[int]:
        M = len(s1)
        N = len(s2)
        s1.sort()
        s2.sort()
        p1 = 0
        p2 = 0

        while p1 < M and p2 < N:
            st = max(s1[p1][0], s2[p2][0])
            end = min(s1[p1][1], s2[p2][1])
            if end - st >= d:
                return [st, st + d]
            if s1[p1][1] < s2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []
    

    def minAvailableDuration(self, s1: list[list[int]], s2: list[list[int]], d: int) -> list[int]:
        hq = []

        for s, e in (s1 + s2):
            if e - s >= d:
                hq.append((s, e))
        heapq.heapify(hq)

        while len(hq) > 1:
            s1, e1 = heapq.heappop(hq)
            s2, e2 = hq[0]
            if e1 >= s2 + d:
                return [s2, s2+d]
        return []
