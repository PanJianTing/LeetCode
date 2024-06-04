from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt_map = defaultdict(int)
        res = 0
        add_one = 0

        for c in s:
            cnt_map[c] += 1

        for k in cnt_map.keys():
            if cnt_map[k] & 1:
                add_one = 1
                res += (cnt_map[k] - 1)
            else:
                res += cnt_map[k]

        return res + add_one
    
    def longestPalindrome(self, s: str) -> int:
        N = len(s)
        cnt_map = defaultdict(int)

        odd_cnt = 0

        for c in s:
            cnt_map[c] += 1
            if cnt_map[c] & 1:
                odd_cnt += 1
            else:
                odd_cnt -= 1
        
        if odd_cnt > 0:
            return N - odd_cnt + 1
        return N
    
    def longestPalindrome(self, s: str) -> int:
        res = 0
        char_set = set()

        for c in s:
            if c in char_set:
                res += 2
                char_set.remove(c)
            else:
                char_set.add(c)
        
        return res + (1 if char_set else 0)

print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("ccccdd"))
print(Solution().longestPalindrome("a"))