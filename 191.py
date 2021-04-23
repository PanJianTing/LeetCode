class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        
        while n > 0:
            print(n)
            if n & 1 == 1:
                i += 1
            n >>= 1
        return i


print(Solution.hammingWeight(Solution(), 11111111111111111111111111111111))