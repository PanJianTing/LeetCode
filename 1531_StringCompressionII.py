from functools import cache

class Solution:
    # MLE
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(idx, cur, last_cnt, remain) -> int:
            if idx == N:
                if remain == 0:
                    if last_cnt <= 1:
                        return last_cnt
                    elif 2 <= last_cnt <= 9:
                        return 2
                    elif 10 <= last_cnt <= 99:
                        return 3
                    else:
                        return 4
                return float('inf')
            
            delete = dp(idx+1, cur, last_cnt, remain-1)
            if cur == s[idx]:
                keep = dp(idx+1, cur, last_cnt+1, remain)
            else:
                keep = dp(idx+1, s[idx], 1, remain)
                if last_cnt <= 1:
                    keep += last_cnt
                elif 2 <= last_cnt <= 9:
                    keep += 2
                elif 10 <= last_cnt <= 99:
                    keep += 3
                else:
                    keep += 4
            # keep = dp(idx+1, curStr+s[idx], remain)
            # delete = dp(idx+1, curStr, remain-1)
            
            return min(keep, delete)
        N = len(s)
        return dp(0, "", 0, k)
    

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        needAdd = set([1,9,99])
        @cache
        def dp(i, cur, last_cnt, remain) -> int:
            if remain < 0:
                return float('inf')
            if i == N:
                return 0
            
            delete = dp(i+1, cur, last_cnt, remain-1)
            if cur == s[i]:
                keep = dp(i+1, cur, last_cnt+1, remain)
                if last_cnt in needAdd:
                    keep += 1
            else:
                keep = dp(i+1, s[i], 1, remain) + 1

            return min(keep, delete)
        
        return dp(0, "", 0, k)

    
    

print(Solution().getLengthOfOptimalCompression('aaabcccd', 2))
print(Solution().getLengthOfOptimalCompression('a', 1))
print(Solution().getLengthOfOptimalCompression('aaaaaaaaaaaaaa', 0))
