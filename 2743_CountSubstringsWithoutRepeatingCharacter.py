from collections import defaultdict
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        N = len(s)
        l = 0
        res = 1
        idx_map = defaultdict(int)
        idx_map[s[0]] = 0
        
        for r in range(1, N):
            if s[r] in idx_map:
                l = max(l ,idx_map[s[r]] + 1)
            idx_map[s[r]] = r
            res += r - l + 1
        return res
    
    def numberOfSpecialSubstrings(self, s: str) -> int:
        N = len(s)
        freq = [0] * 26
        l = 0
        res = 0

        for r in range(N):
            freq[ord(s[r]) - ord('a')] += 1

            while freq[ord(s[r]) - ord('a')] > 1:
                freq[ord(s[l]) - ord('a')] -= 1
                l += 1

            res += r - l + 1
        return res
            
    

print(Solution().numberOfSpecialSubstrings('abcd'))     #10
print(Solution().numberOfSpecialSubstrings('ooo'))      #3
print(Solution().numberOfSpecialSubstrings('abab'))     #7
print(Solution().numberOfSpecialSubstrings('bddqc'))    #9
print(Solution().numberOfSpecialSubstrings('fiifj'))    #9