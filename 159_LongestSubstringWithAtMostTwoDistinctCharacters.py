from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s) -> int:
        i = 0
        cnt_map = defaultdict(int)
        ans = 0

        for j, c in enumerate(s):
            cnt_map[c] += 1
            while len(cnt_map) > 2:
                delC = s[i]
                cnt_map[delC] -= 1
                if cnt_map[delC] == 0:
                    del cnt_map[delC]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
    
    def lengthOfLongestSubstringTwoDistinct(self, s) -> int:
        i = 0
        idx_map = defaultdict(int)
        ans = 0

        for j, c in enumerate(s):
            idx_map[c] = j
            if len(idx_map) > 2:
                del_idx = min(idx_map.values())
                del idx_map[s[del_idx]]
                i = del_idx + 1
            
            ans = max(ans, j - i + 1)
        
        return ans

    
print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))