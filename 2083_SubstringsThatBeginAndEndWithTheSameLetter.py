from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_map = defaultdict(int)
        res = 0

        for c in s:
            char_map[c] += 1

        for n in char_map.values():
            res += ((n * (n+1)) >> 1)

        return res
    
    def numberOfSubstrings(self, s: str) -> int:
        char_map = defaultdict(int)
        res = 0

        for c in s:
            char_map[c] += 1
            res += char_map[c]

        return res
    
print(Solution().numberOfSubstrings("abcba"))
print(Solution().numberOfSubstrings("abacad"))
print(Solution().numberOfSubstrings("a"))