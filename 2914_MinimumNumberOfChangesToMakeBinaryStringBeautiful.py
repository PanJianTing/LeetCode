class Solution:
    def minChanges(self, s: str) -> int:
        N = len(s)
        ans = 0

        for i in range(0, N, 2):
            if s[i] != s[i+1]:
                ans += 1
        
        return ans
    

    def minChanges(self, s: str) -> int:
        cur_char = s[0]
        cur_count = 0
        ans = 0

        for c in s:
            if c == cur_char:
                cur_count += 1
                continue
            
            if cur_count & 1 == 0:
                cur_count = 1
            else:
                cur_count = 0
                ans += 1
            cur_char = c
        
        return ans
    
print(Solution().minChanges("1010"))
    

        
        