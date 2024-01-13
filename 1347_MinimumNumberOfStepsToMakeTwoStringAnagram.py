from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_map = defaultdict(int)
        ans = 0

        for c in s:
            cnt_map[c] += 1
        for c in t:
            if c in cnt_map and cnt_map[c] > 0:
                cnt_map[c] -= 1
        for num in cnt_map.values():
            ans += num
        return ans
    

    def minSteps(self, s: str, t: str) -> int:
        N = len(s)
        cnt_map = defaultdict(int)
        ans = 0

        for i in range(N):
            cnt_map[s[i]] += 1
            cnt_map[t[i]] -= 1
        
        for cnt in cnt_map.values():
            ans += cnt if cnt > 0 else 0
        
        return ans
    
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        
        for c in set(t):
            diff = t.count(c) - s.count(c)
            ans += diff if diff > 0 else 0
        return ans


    
print(Solution().minSteps("bab", "aba"))
print(Solution().minSteps("leetcode", "practice"))
print(Solution().minSteps("anagram", "mangaar"))
