from functools import cache

class Solution:

    def numOfArrays(self, n, m, k) -> int:

        @cache
        def buildArray(i, max_num, remain):
            if i == n:
                if remain == 0:
                    return 1
                else:
                    return 0
            if remain < 0:
                return 0
            ans = 0
            for num in range(1, m+1):
                if num > max_num:
                    ans += buildArray(i+1, num, remain - 1)
                else:
                    ans += buildArray(i+1, max_num, remain)

            return ans
        
        
        return buildArray(0, 0, k) % (10 ** 9 + 7)

        
    
print(Solution().numOfArrays(2,3,1))
print(Solution().numOfArrays(5,2,3))
print(Solution().numOfArrays(9,1,1))
