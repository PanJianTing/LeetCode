from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        N = len(high)
        low = low.zfill(N)
        pre_len = N - len(s)

        @cache
        def dfs(i, limit_low, limit_high):
            if i == N:
                return 1
            
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            
            res = 0
            
            if i < pre_len:

                for digit in range(lo, min(limit, hi) + 1):
                    res += dfs(i+1, limit_low and digit == lo, limit_high and digit == hi)
            else:

                x = int(s[i - pre_len])

                if lo <= x <= min(hi, limit):
                    res = dfs(i+1, limit_low and x == lo, limit_high and x == hi)
            
            return res
        return dfs(0, True, True)
    



    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start - 1)
        high = str(finish)


        def calculation(cur):
            if len(cur) < len(s):
                return 0
            
            if len(cur) == len(s):
                return 1 if cur >= s else 0

            suffix = cur[(len(cur) - len(s)):]
            count = 0
            pre_len = len(cur) - len(s)

            for i in range(pre_len):
                cur_d = int(cur[i])
                if limit < cur_d:
                    count += (limit+1) ** (pre_len - i)
                    return count
                count += cur_d * ((limit+1) ** (pre_len - 1 - i))

            if suffix >= s:
                count += 1
            return count
        return calculation(high) - calculation(low)
    

    # def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
    #     start_ = str(start - 1)
    #     finish_ = str(finish)
    #     return self.calculate(finish_, s, limit) - self.calculate(start_, s, limit)

    # def calculate(self, x: str, s: str, limit: int) -> int:
    #     if len(x) < len(s):
    #         return 0
    #     if len(x) == len(s):
    #         return 1 if x >= s else 0

    #     suffix = x[len(x) - len(s) :]
    #     count = 0
    #     pre_len = len(x) - len(s)

    #     for i in range(pre_len):
    #         if limit < int(x[i]):
    #             count += (limit + 1) ** (pre_len - i)
    #             return count
    #         count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

    #     if suffix >= s:
    #         count += 1

    #     return count
    
# print(Solution().numberOfPowerfulInt(1, 6000, 4, "124"))
# print(Solution().numberOfPowerfulInt(15, 215, 6, "10"))
print(Solution().numberOfPowerfulInt(1, 971, 9, "41"))
                
