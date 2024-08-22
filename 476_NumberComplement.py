from math import floor, log2

class Solution:
    def findComplement(self, num: int) -> int:
        cur = 1
        total_num = 0
        temp = num

        while num > 0:
            total_num += cur
            cur <<= 1
            num >>= 1
        
        return total_num - temp
    
    def findComplement(self, num: int) -> int:
        bit = 1
        todo = num

        while todo > 0:
            num ^= bit
            bit <<= 1
            todo >>= 1
        
        return num
    
    def findComplement(self, num: int) -> int:
        N = floor(log2(num)) + 1

        bitmask = (1 << N) - 1

        return num ^ bitmask
    
    def findComplement(self, num: int) -> int:
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)

        return num ^ bitmask

    
print(Solution().findComplement(5))
print(Solution().findComplement(2))
print(Solution().findComplement(1))