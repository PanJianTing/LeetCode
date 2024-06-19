class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if N < m * k:
            return -1
        if N == m * k:
            return max(bloomDay)

        def check(d):
            cur = 0
            res = 0
            for i in range(N):
                if bloomDay[i] <= d:
                    cur += 1
                else:
                    cur = 0
                if cur == k:
                    res += 1
                    cur = 0
            return res
        
        l = min(bloomDay)
        r = max(bloomDay)
        res = r

        while l <= r:
            mid_day = l + ((r-l) >> 1)
            if check(mid_day) >= m:
                res = min(res, mid_day)
                r = mid_day - 1
            else:
                l = mid_day + 1
        return res
    

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if N < m * k:
            return -1
        if N == m * k:
            return max(bloomDay)

        def check(d):
            cur = 0
            res = 0
            for i in range(N):
                if bloomDay[i] <= d:
                    cur += 1
                else:
                    cur = 0
                if cur == k:
                    res += 1
                    cur = 0
            return res
        
        l = min(bloomDay)
        r = max(bloomDay)

        while l < r:
            mid_day = l + ((r-l) >> 1)
            if check(mid_day) >= m:
                r = mid_day
            else:
                l = mid_day + 1
        return l
    
print(Solution().minDays([1,10,3,10,2], 3, 1))
print(Solution().minDays([7,7,7,7,12,7,7], 2, 3))