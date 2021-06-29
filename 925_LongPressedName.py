
from itertools import groupby

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j-1] != typed[j]:
                return False

        return i == len(name)





    def isLongPressedName_my(self, name: str, typed: str) -> bool:

        nameMap = [(i, len(list(v))) for i, v in groupby(name)]
        typeMap = [(i, len(list(v))) for i, v in groupby(typed)]


        if len(nameMap) != len(typeMap):
            return False


        for i,v in enumerate(nameMap):

            if nameMap[i][0] != typeMap[i][0]:
                return False
            
            if nameMap[i][1] > typeMap[i][1]:
                return False


        return True


Solution.isLongPressedName(Solution(), "saeed", "ssaaedd")