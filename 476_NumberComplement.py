from math import log2
from math import floor

class Solution:
    def findComplement(self, num: int) -> int:
        n = floor(log2(num)) + 1
        bitmask = (1 << n) - 1

        return bitmask ^ num


    def findComplement(self, num: int) -> int:

        todo, bit = num, 1

        while todo:
            num = num ^ bit

            bit <<= 1
            todo >>= 1

        return num

    def findComplement(self, num: int) -> int:
        
        max = 1

        while max <= num:
            max <<= 1

        return max - 1 - num

Solution().findComplement(5)
Solution().findComplement(7)