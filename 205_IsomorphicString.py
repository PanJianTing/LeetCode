
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False
        
        charMap = {}
        
        for i in range(len(s)):
            if s[i] in cahrMap:
                if t[i] != charMap[s[i]]:
                    return False
            else:
                charMap[s[i]] = t[i]
        return True
        
        
    def isIsomorphic_my(self, s: str, t: str) -> bool:
        
        setS = set(s)
        setT = set(t)
        
        if len(setS) != len(setT):
            return False
        
        print(setS, setT)
        charMap = {}
        listS = list(s)
        listT = list(t)
        
        # return len(setS) == len(setT)
        
        for i in range(len(listS)):
            if listT[i] not in charMap:
                charMap[listT[i]] = listS[i]

        for i in range(len(listT)):
            if listT[i] in charMap:
                listT[i] = charMap[listT[i]]
        return listS == listT

    
print(Solution.isIsomorphic(Solution(), "add", "egg"))
print(Solution.isIsomorphic(Solution(), "foo", "bar"))
print(Solution.isIsomorphic(Solution(), "paper", "title"))
print(Solution.isIsomorphic(Solution(), "badc", "baba"))
print(Solution.isIsomorphic(Solution(), "bbbaaaba", "aaabbbba"))


print("Hello World!")