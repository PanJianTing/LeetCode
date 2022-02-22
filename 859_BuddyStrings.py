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