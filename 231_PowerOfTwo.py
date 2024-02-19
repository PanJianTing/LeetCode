class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        val = 1
        for _ in range(31):
            if val == n:
                return True
            val *= 2
        return False
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & (-n)) == n
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & (n-1)) == 0

print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))