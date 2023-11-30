class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        
        while n > 0:
            if n & 1 == 1:
                i += 1
            n >>= 1
        return i
    
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            ans += 1
            n &= (n-1)
        return ans
    
    def hammingWeight(self, n: int) -> int:
        ans = 0
        mask = 1
        
        for _ in range(32):
            if (n & mask):
                ans += 1
            mask <<= 1
        return ans




print(Solution().hammingWeight(11))
print(Solution().hammingWeight(128))
print(Solution().hammingWeight(4294967293))