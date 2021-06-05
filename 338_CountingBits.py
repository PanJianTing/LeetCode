class Solution:
    def bits(self, n) -> int:

        result = 0

        while n > 0:
            if n % 2 == 1:
                result += 1
            n //= 2

        return result

    def countBits(self, n: int) -> list[int]:

        bitList = []

        for i in range(n+1):

            bitList.append(self.bits(i))
        
        return bitList

