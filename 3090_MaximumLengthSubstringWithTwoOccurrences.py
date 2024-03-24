from collections import defaultdict
import heapq

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        N = len(s)
        ans = 0

        for st in range(N):
            for end in range(st+1, N+1):
                cnt_map = defaultdict(int)
                for i in range(st, end):
                    cnt_map[s[i]] += 1

                isvalid = True
                for cnt in cnt_map.values():
                    if cnt > 2:
                        isvalid = False
                        break
                
                if isvalid:
                    ans = max(ans , end-st)
        return ans
    
    def maximumLengthSubstring(self, s: str) -> int:
        N = len(s)
        ans = 0

        def check(s):
            cnt_map = defaultdict(int)

            for c in s:
                cnt_map[c] += 1
                if cnt_map[c] > 2:
                    return False
            return True

        for i in range(N):
            for j in range(i, N):
                if check(s[i:j+1]):
                    ans = max(ans, j-i+1)
        return ans
    
    def maximumLengthSubstring(self, s: str) -> int:
        N = len(s)
        cnt_map = defaultdict(int)
        ans = 0
        i = 0
        j = 0

        while j < N:
            cnt_map[s[j]] += 1
            while cnt_map[s[j]] > 2:
                cnt_map[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans


    
print(Solution().maximumLengthSubstring("bcba"))
print(Solution().maximumLengthSubstring("bcbbbcba"))
print(Solution().maximumLengthSubstring("aaaa"))
                        
                        

