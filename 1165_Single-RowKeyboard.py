from collections import defaultdict

class Solution:
    def calculateTime(self, keyboard, word) -> int:
        idx_map = defaultdict(int)
        cur = 0
        ans = 0

        for idx, c in enumerate(keyboard):
            idx_map[c] = idx
        
        for c in word:
            next_idx = idx_map[c]
            ans += abs(next_idx - cur)
            cur = next_idx
        return ans
    

print(Solution().calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
print(Solution().calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))
            