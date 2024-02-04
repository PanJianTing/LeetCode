from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        N = len(s)
        left = 0
        right = 0
        need_map = defaultdict(int)
        cnt_map = defaultdict(int)

        for c in t:
            need_map[c] += 1

        def check() -> bool:
            for c in need_map.keys():
                if cnt_map[c] < need_map[c]:
                    return False
            return True
        
        for right in range(N):
            cnt_map[s[right]] += 1
            while check():
                if ans == "" or len(s[left: right+1]) < len(ans):
                    ans = s[left: right+1]
                cnt_map[s[left]] -= 1
                left += 1
        return ans
    

    def minWindow(self, s: str, t: str) -> str:
        ans_st = -1
        ans_end = -1
        N = len(s)
        check_cnt = 0
        left = 0
        right = 0
        need_map = defaultdict(int)
        cnt_map = defaultdict(int)
        is_satisfy = 0

        for c in t:
            need_map[c] += 1
        check_cnt = len(need_map.keys())
        
        for right in range(N):
            cur = s[right]
            cnt_map[cur] += 1
            if need_map[cur] == cnt_map[cur]:
                is_satisfy += 1
            while is_satisfy == check_cnt:
                if ans_st == -1 or (right - left) < (ans_end - ans_st):
                    ans_st = left
                    ans_end = right
                cnt_map[s[left]] -= 1
                if cnt_map[s[left]] < need_map[s[left]]:
                    is_satisfy -= 1
                left += 1
        return "" if ans_st == -1 else s[ans_st:ans_end+1]
    

    def minWindow(self, s: str, t: str) -> str:
        ans_st = -1
        ans_end = -1
        N = len(s)
        check_cnt = 0
        left = 0
        need_map = defaultdict(int)
        cnt_map = defaultdict(int)
        is_satisfy = 0

        new_s = []

        for c in t:
            need_map[c] += 1
        check_cnt = len(need_map.keys())
        

        for i, c in enumerate(s):
            if c in need_map.keys():
                new_s.append((i, c))

        N = len(new_s)

        for right in range(N):
            cur_idx, cur = new_s[right]
            cnt_map[cur] += 1
            if need_map[cur] == cnt_map[cur]:
                is_satisfy += 1
            while is_satisfy == check_cnt:
                cur_left, cur_left_c = new_s[left]
                if ans_st == -1 or (cur_idx - cur_left) < (ans_end - ans_st):
                    ans_st = cur_left
                    ans_end = cur_idx
                cnt_map[cur_left_c] -= 1
                if cnt_map[cur_left_c] < need_map[cur_left_c]:
                    is_satisfy -= 1
                left += 1
        return "" if ans_st == -1 else s[ans_st:ans_end+1]
    

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "a"))
print(Solution().minWindow("a", "aa"))
print(Solution().minWindow("aa", "aa"))
print(Solution().minWindow("a", "b"))