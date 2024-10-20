from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0

        for i in range(N):
            for j in range(i, N):
                temp = [0] * 26
                cur_s = s[i:j+1]
                for c in cur_s:
                    cur_idx = ord(c) - ord('a')
                    temp[cur_idx] += 1
                    if temp[cur_idx] == k:
                        ans += 1
                        break

        return ans
    
    def numberOfSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        cnt_list = [0] * 26
        l = 0

        ans = 0
        for r in range(N):
            cur_idx = ord(s[r]) - ord('a')
            cnt_list[cur_idx] += 1
            while l <= r:
                goal = False
                for n in cnt_list:
                    if n >= k:
                        goal = True
                        break
                if goal:
                    ans += N - r
                    cnt_list[ord(s[l]) - ord('a')] -= 1
                    l += 1
                else:
                    break

        return ans
    

    def numberOfSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        res = N * (N+1) // 2
        cnt_map = defaultdict(int)
        l = 0

        for r in range(N):
            cur_c = s[r]
            cnt_map[cur_c] += 1
            while cnt_map[cur_c] >= k:
                cnt_map[s[l]] -= 1
                l += 1
            res -= r - l + 1
        return res

    


print(Solution().numberOfSubstrings('abacb', 2))
print(Solution().numberOfSubstrings('abced', 1))
print(Solution().numberOfSubstrings('ajsrhoebe', 2))