from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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

    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False
        
        charMap = {}
        
        for i in range(len(s)):
            if s[i] in charMap:
                if t[i] != charMap[s[i]]:
                    return False
            else:
                charMap[s[i]] = t[i]
        return True
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(str)
        t_map = defaultdict(str)
        res_s = []
        res_t = []

        for sc, tc in zip(s, t):
            s_map[sc] = tc
            t_map[tc] = sc
        
        for sc, tc in zip(s, t):
            res_s.append(s_map[sc])
            res_t.append(t_map[tc])

        return t == ''.join(res_s) and s == ''.join(res_t)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        M = len(set(s))
        N = len(set(t))
        char_set = set()

        for sc, tc in zip(s, t):
            char_set.add((sc, tc))

        return M == N == len(char_set)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(str)
        t_map = defaultdict(str)

        for sc, tc in zip(s, t):
            if sc not in s_map and tc not in t_map:
                s_map[sc] = tc
                t_map[tc] = sc
            else:
                if s_map[sc] == tc and t_map[tc] == sc:
                    continue
                else:
                    return False
                
        return True
    
    def isIsomorphic(self, s: str, t: str) -> bool:

        def map_char(ss) -> str:
            char_map = defaultdict(int)
            res = []
            for i, s in enumerate(ss):
                if s not in char_map:
                    char_map[s] = i
                    
                res.append(str(char_map[s]))
            return '.'.join(res)
        
        return map_char(s) == map_char(t)

    
print(Solution().isIsomorphic("add", "egg"))
print(Solution().isIsomorphic("foo", "bar"))
print(Solution().isIsomorphic("paper", "title"))
print(Solution().isIsomorphic("badc", "baba"))
print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
print(Solution().isIsomorphic('paper', 'ttile'))