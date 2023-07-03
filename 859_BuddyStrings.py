class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # if length differ
        if len(s) != len(goal):
            return False

        # if s == goal, check same char appear twice
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
        else:
            # if s != goal, check if only two char differ and if reverse is same
            pairs = []

            for a, b in zip(s, goal):
                if a != b:
                    pairs.append((a,b))

            
            if len(pairs) == 2:
                return pairs[0] == pairs[1][::-1]
        return False
                

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # if length differ
        if len(s) != len(goal):
            return False

        # if s == goal, check same char appear twice
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            # if s != goal, check if only two char differ and if reverse is same
            sIndex = set()

            for index in range(0, len(s)):
                if s[index] != goal[index]:
                    sIndex.add(index)
            
            if len(sIndex) == 2:
                indexArray = list(sIndex)
                index1 = indexArray[0]
                index2 = indexArray[1]

                if s[index1] == goal[index2] and s[index2] == goal[index1]:
                    return True

        return False
    
# 2023/07/03
from collections import defaultdict

class Solution:
    def buddyStrings(self, s, goal) -> bool:
        M = len(s)
        N = len(goal)
        goal = list(goal)

        if not (M == N):
            return False

        for i in range(M):
            for j in range(i+1, N):
                tempStr = list(s)
                tempStr[i], tempStr[j] = tempStr[j], tempStr[i]
                if tempStr == goal:
                    return True
        return False
                
    def buddyStrings(self, s: str, goal: str) -> bool:
        M = len(s)
        N = len(goal)
        if (M == N) == False:
            return False

        m = defaultdict(int)
        goal = list(goal)

        for i in range(M):
            m[s[i]] = i
        
        for i in range(N):
            c = goal[i]
            j = m[c]
            if i == j:
                continue
            tempStr = list(s)
            tempStr[i], tempStr[j] = tempStr[j], tempStr[i]
            if goal == tempStr:
                return True
            
        return False
    
    def buddyStrings(self, s, goal) -> bool:
        
        if (len(s) == len(goal)) == False:
            return False
        
        if s == goal:
            chars = set()
            for c in s:
                if c in chars:
                    return True
                chars.add(c)
            return False
        
        diff = []
        for a,b in zip(s, goal):
            if (a == b) == False:
                diff.append([a,b])
        
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        
        return False
    
    def buddyStrings(self, s, goal) -> bool:
        M = len(s)
        N = len(goal)
        
        if (M == N) == False:
            return False
        
        if s == goal:
            check = set()
            for c in s:
                if c in check:
                    return True
                check.add(c)
            return False
        
        firstIdx = -1
        secondIdx = -1

        for i in range(0, len(s)):
            a = s[i]
            b = goal[i]
            if (a == b) == False:
                if firstIdx == -1:
                    firstIdx = i
                elif secondIdx == -1:
                    secondIdx = i
                else:
                    return False
                
        if secondIdx == -1:
            return False
                
        return s[firstIdx] == goal[secondIdx] and s[secondIdx] == goal[firstIdx]
    
    def buddyStrings(self, s, goal) -> bool:
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(s): return True
        dif = [(a,b) for a, b in zip(s, goal) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]

                    

print(Solution().buddyStrings("ab", "ab"))
print(Solution().buddyStrings("aa", "aa"))
print(Solution().buddyStrings("abcd", "badc"))
print(Solution().buddyStrings("abab", "abab"))