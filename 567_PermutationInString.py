class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        candidateIndex = []
        s1Map = {}

        for c in s1:
            if c in s1Map:
                s1Map[c] += 1
            else:
                s1Map[c] = 1

        for i in range(0, len(s2)-lenS1+1):
            w2 = s2[i]
            if w2 in s1:
                candidateIndex.append([i, i+lenS1])

        candidateMapList = []

        for index in candidateIndex:
            checkStr = s2[index[0]:index[1]]
            checkMap = {}
            for c in checkStr:
                if c in checkMap:
                    checkMap[c] += 1
                else:
                    checkMap[c] = 1
            
            candidateMapList.append(checkMap)
        
        for candidateMap in candidateMapList:
            sameKeyValue = 0
            for key in s1Map.keys():
                if key in candidateMap:
                    if candidateMap[key] == s1Map[key]:
                        sameKeyValue += 1
            if sameKeyValue == len(candidateMap.keys()):
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        lenS1 = len(s1)
        for i in range(0, len(s2) - lenS1 + 1):
            substr = s2[i:i+lenS1]
            if s1 == "".join(sorted(substr)):
                return True
        return False

    def match(self, s1Map: list[int], s2Map: list[int]) -> bool:

        for i in range(0, 26):
            if s1Map[i] != s2Map[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Map = [0] * 26
        s2Map = [0] * 26

        base = ord('a')
        lenS1 = len(s1)

        for i in range(0, lenS1):
            s1Map[ord(s1[i]) - base] += 1
            s2Map[ord(s2[i]) - base] += 1

        for i in range(0, len(s2) - lenS1):
            if self.match(s1Map, s2Map):
                return True
            s2Map[ord(s2[i + lenS1]) - base] += 1
            s2Map[ord(s2[i]) - base] -= 1


        return self.match(s1Map, s2Map)


print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
print(Solution().checkInclusion("ab", "ab"))
print(Solution().checkInclusion("hello", "ooolleoooleh"))
print(Solution().checkInclusion("adc", "dcda"))