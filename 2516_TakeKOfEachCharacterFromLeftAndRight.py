from collections import defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)

        def dp(cur_l, cur_r, cur_min, cur_map):
            if cur_map['a'] >= k and cur_map['b'] >= k and cur_map['c'] >= k:
                return cur_min
            
            if cur_l > cur_r:
                return float('inf')
            
            cur_map[s[cur_l]] += 1
            l_min = dp(cur_l+1, cur_r, 1+cur_min, cur_map)
            cur_map[s[cur_l]] -= 1

            cur_map[s[cur_r]] += 1
            r_min = dp(cur_l, cur_r-1, 1+cur_min, cur_map)
            cur_map[s[cur_r]] -= 1

            return min(l_min, r_min)
        ans = dp(0, N-1, 0, defaultdict(int))
        return -1 if ans == float('inf') else ans
    

    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)
        cnt_map = defaultdict(int)

        for c in s:
            cnt_map[c] += 1
        
        if not (cnt_map['a'] >= k and cnt_map['b'] >= k and cnt_map['c'] >= k):
            return -1
        
        l = 0
        max_window_size = 0
        window_cnt = defaultdict(int)

        for r in range(N):
            cur_c = s[r]
            window_cnt[cur_c] += 1

            while l <= r and (cnt_map['a'] - window_cnt['a'] < k or cnt_map['b'] - window_cnt['b'] < k or cnt_map['c'] - window_cnt['c'] < k):
                window_cnt[s[l]] -= 1
                l += 1
            
            max_window_size = max(max_window_size, r-l+1)
        
        return N - max_window_size
    


print(Solution().takeCharacters('aabaaaacaabc', 2))
            