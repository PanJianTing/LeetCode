from collections import defaultdict

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        res = 0
        
        for i in range(N):
            for j in range(i, N):
                cur = s[i:j+1]
                if cur.count("0") <= k or cur.count("1") <= k:
                    res += 1
        return res
    

    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        res = 0

        for i in range(N):
            count1 = 0
            count0 = 0
            for j in range(i, N):
                if s[j] == '0':
                    count0 += 1
                else:
                    count1 += 1
                
                if count0 <= k or count1 <= k:
                    res += 1
        return res
    

print(Solution().countKConstraintSubstrings("10101", 1))
print(Solution().countKConstraintSubstrings("1010101", 2))