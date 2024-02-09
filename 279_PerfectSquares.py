import math
from math import sqrt
from functools import cache
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_nums = [i * i for i in range(1, int(sqrt(n))+1)]

        @cache
        def dp(num):
            if num in perfect_nums:
                return 1
            
            res = float('inf')
            for i in perfect_nums:
                if num - i < 0:
                    break
                res = min(res, dp(num-i)+1)
            
            return res
        return dp(n)
    
    def numSquares(self, n: int) -> int:
        N = n+1
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        perfect_nums = []

        for num in range(1, N):
            if sqrt(num).is_integer():
                dp[num] = 1
                perfect_nums.append(num)
            else:
                for i in perfect_nums:
                    dp[num] = min(dp[num], dp[i] + dp[num-i])
        return dp[n]


    def numSquares(self, n: int) -> int:
        N = n+1
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        perfect_nums = [i*i for i in range(1, int(sqrt(n))+1)]

        for num in range(1, N):
            if num in perfect_nums:
                dp[num] = 1
            else:
                for i in perfect_nums:
                    if num - i < 0:
                        break
                    dp[num] = min(dp[num], dp[i] + dp[num-i])
        return dp[n]
    
    def numSquares(self, n: int) -> int:
        perfect_nums = set([i*i for i in range(1, int(sqrt(n)) + 1)])

        def is_divid(cnt, num):
            if cnt == 1:
                if num in perfect_nums:
                    return True
                return False

            for i in perfect_nums:
                if is_divid(cnt-1, num-i):
                    return True
            return False

        for count in range(1, n+1):
            if is_divid(count, n):
                return count
        return n
    

    def numSquares(self, num) -> int:
        perfect_nums = [i*i for i in range(1, int(sqrt(num)) + 1)]
        q = deque()
        q.append(num)

        ans = 0
        visit = set()
        visit.add(num)

        while q:
            ans += 1
            N = len(q)
            for _ in range(N):
                cur = q.popleft()

                if cur in perfect_nums:
                    return ans

                for i in perfect_nums:
                    if cur - i < 0:
                        break
                    remainder = cur - i
                    if remainder not in visit:
                        visit.add(remainder)
                        q.append(remainder)
        return ans
    
    def numSquares(self, num) -> int:
        perfect_nums = [i*i for i in range(1, int(sqrt(num)) + 1)]
        q = set()
        q.add(num)

        ans = 0

        while q:
            ans += 1
            next_q = set()
            for cur in q:
                if cur in perfect_nums:
                    return ans

                for i in perfect_nums:
                    if cur - i < 0:
                        break
                    remainder = cur - i
                    next_q.add(remainder)
            
            q = next_q
        return ans
    
    def numSquares(self, n) -> int:
        check_four = n
        while check_four % 4 == 0:
            check_four /= 4
        if check_four % 8 == 7:
            return 4
        

        perfect_nums = set([i*i for i in range(1, int(sqrt(n))+1)])
        if n in perfect_nums:
            return 1
        
        for i in perfect_nums:
            if (n - i) in perfect_nums:
                return 2
        return 3
    
    def numSquares(self, num) -> int:
        check_four = num
        while check_four & 3 == 0:
            check_four >>= 2
        if check_four % 8 == 7:
            return 4
        
        perfect_nums = [i*i for i in range(1, int(sqrt(num)) + 1)]

        if num in perfect_nums:
            return 1
        
        for i in perfect_nums:
            if (num - i) in perfect_nums:
                return 2
        return 3

            
        

# print(Solution().numSquares(1))
# print(Solution().numSquares(2))
# print(Solution().numSquares(3))
# print(Solution().numSquares(4))
# print(Solution().numSquares(5))
# print(Solution().numSquares(6))
# print(Solution().numSquares(7))
# print(Solution().numSquares(8))
# print(Solution().numSquares(9))
print(Solution().numSquares(12))
print(Solution().numSquares(5156))
