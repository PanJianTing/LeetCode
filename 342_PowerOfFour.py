from math import log2

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n % 4:
                return False
            n //= 4
        return True
    
    def isPowerOfFour(self, n: int) -> bool:

        fourList = [1]
        for _ in range(15):
            fourList.append(fourList[-1] << 2)
        return n in fourList
    
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (log2(n) % 2 == 0)
    
    # power of two => (n & n-1) == 0
    # 10101010...1010 => 0xaaaaaaaa == 0 找奇數位置
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 and (n & 0xaaaaaaaa) == 0
    
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 and (n % 3) == 1

    

print(Solution().isPowerOfFour(5))
            
