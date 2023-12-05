class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1


    def numberOfMatches(self, n: int) -> int:
        ans = 0

        while n > 1:
            if n % 2 == 0:
                ans += n//2
                n >>= 1
            else:
                ans += n//2
                n >>= 1
                n += 1

        return ans

print(Solution().numberOfMatches(7))
                