class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if (n == 0):
            return 0
        k = 0
        cur = 1
        while (cur << 1) <= n:
            cur <<= 1
            k += 1
        return (1 << (k+1)) - 1 - self.minimumOneBitOperations(n ^ cur)

print(Solution().minimumOneBitOperations(5))