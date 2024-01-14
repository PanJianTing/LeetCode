from collections import defaultdict

class Solution:
    def closeStrings(self, s1, s2) -> bool:
        if len(s1) != len(s2):
            return False
        
        cnt1_map = defaultdict(int)
        cnt2_map = defaultdict(int)

        for c1, c2 in zip(s1, s2):
            cnt1_map[c1] += 1
            cnt2_map[c2] += 1
        
        return (cnt1_map.keys() == cnt2_map.keys()) and (sorted(cnt1_map.values()) == sorted(cnt2_map.values()))
    
    def closeStrings(self, s1, s2) -> bool:
        if len(s1) != len(s2):
            return False
        
        cnt1_list = [0] * 26
        cnt2_list = [0] * 26

        for c1, c2 in zip(s1, s2):
            cnt1_list[ord(c1) - ord('a')] += 1
            cnt2_list[ord(c2) - ord('a')] += 1

        for i in range(26):
            if (cnt1_list[i] == 0 and cnt2_list[i] != 0) or (cnt1_list[i] != 0 and cnt2_list[i] == 0):
                return False
            
        return sorted(cnt1_list) == sorted(cnt2_list)
    
    def closeStrings(self, s1, s2) -> bool:
        if len(s1) != len(s2):
            return False
        
        cnt1_map = defaultdict(int)
        cnt2_map = defaultdict(int)
        s1Bit = 0
        s2Bit = 0

        for c1, c2 in zip(s1, s2):
            cnt1_map[c1] += 1
            cnt2_map[c2] += 1
            s1Bit = s1Bit | (1 << (ord(c1) - ord('a')))
            s2Bit = s2Bit | (1 << (ord(c2) - ord('a')))
        
        if s1Bit != s2Bit:
            return False
        return sorted(cnt1_map.values()) == sorted(cnt2_map.values())
    
    def closeStrings(self, s1, s2) -> bool:
        if len(s1) != len(s2):
            return False
        
        char_set = set(s1)

        if char_set != set(s2):
            return False
        
        cnt1_list = []
        cnt2_list = []
        for c in char_set:
            cnt1_list.append(s1.count(c))
            cnt2_list.append(s2.count(c))
        
        return sorted(cnt1_list) == sorted(cnt2_list)

    
print(Solution().closeStrings("abc", "bca"))            # T
print(Solution().closeStrings("a", "aa"))               # F
print(Solution().closeStrings("cabbba", "abbccc"))      # T
print(Solution().closeStrings("abbbzcf", "babzzcz"))    # F
print(Solution().closeStrings("uau", "ssx"))            # F
print(Solution().closeStrings("abbzzca", "babzzcz"))    # F