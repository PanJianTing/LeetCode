class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cur_black = 0

        for c in s:
            if c == '0':
                ans += cur_black
            else:
                cur_black += 1
        return ans
    
    def minimumSteps(self, s: str) -> int:
        ans = 0
        white_idx = 0

        for i, c in enumerate(s):
            if c == '0':
                ans += i - white_idx
                white_idx += 1
        return ans

    

    
print(Solution().minimumSteps("101"))
print(Solution().minimumSteps("100"))
print(Solution().minimumSteps("0111"))
