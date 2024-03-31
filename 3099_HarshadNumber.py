class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        sum_digits = 0
        temp = x

        while x > 0:
            sum_digits += x % 10
            x //= 10
        
        return sum_digits if temp % sum_digits == 0 else -1