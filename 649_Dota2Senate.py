from collections import deque

class Solution:

    def ban(self, senateList: list, c: str, idx: int) -> bool:
        checkCnt = 0
        maxCheck = len(senateList)
        p = idx % maxCheck
        remove = False

        while checkCnt < maxCheck:
            if senateList[p] == c:
                del senateList[p]
                remove = True
                break
            checkCnt += 1
            p = (p+1) % maxCheck
        
        return remove


    def predictPartyVictory(self, senate: str) -> str:

        rCnt = 0
        dCnt = 0
        senateList = list(senate)
        idx = 0

        for s in senateList:
            if 'R' == s:
                rCnt += 1
            else:
                dCnt += 1

        while rCnt > 0 and dCnt > 0:

            now = senateList[idx]
            if now == "R":
                if self.ban(senateList, "D", idx+1):
                    dCnt -= 1
            else:
                if self.ban(senateList, "R", idx+1):
                    rCnt -= 1
            idx += 1
            if idx >= len(senateList):
                idx = 0


        if rCnt == 0:
            return "Dire"
        return "Radiant"
    
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ = deque()
        dQ = deque()
        cycle = len(senate)

        for i,s in enumerate(senate):
            if s == "R":
                rQ.append(i)
            else:
                dQ.append(i)

        while rQ and dQ:
            r,d = rQ.popleft(), dQ.popleft()

            if r < d:
                rQ.append(r+cycle)
            else:
                dQ.append(d+cycle)

        return "Radiant" if rQ else "Dire"
    
class Sloution:
    def predictPartyVictory(self, senate: str) -> str:
        rCnt, dCnt = 0, 0
        rBan, dBan = 0, 0
        q = deque()

        for s in senate:
            q.append(s)
            if s == "R":
                rCnt += 1
            else:
                dCnt += 1
        
        while rCnt > 0 and dCnt > 0:
            cur = q.popleft()

            if cur == "D":
                if dBan > 0:
                    dBan -= 1
                    dCnt -= 1
                else:
                    rBan += 1
                    q.append(cur)
            else:
                if rBan > 0:
                    rBan -= 1
                    rCnt -= 1
                else:
                    dBan += 1
                    q.append(cur)

        return 'Radiant' if rCnt > 0 else "Dire"




print(Solution().predictPartyVictory("RD"))
print(Solution().predictPartyVictory("RDD"))
print(Solution().predictPartyVictory("DDRRR"))
