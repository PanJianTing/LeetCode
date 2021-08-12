class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:

        for i in range(1, n):
            count = n - i
            if "0" not in str(i) and "0" not in str(count):
                return [i, count]

        return [1, n-1]



    # Down is My Solution
    def isHaveZero(self, n: int) -> bool:

        while n > 0:
            if n % 10 == 0:
                return True
            else:
                n //= 10
        
        return False


    def getNoZeroIntegers(self, n: int) -> list[int]:

        for i in range(1, n):
            count = n - i
            if self.isHaveZero(count) == False and self.isHaveZero(i) == False:
                return [i, count]

        return [1, n-1]