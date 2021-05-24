class Solution:
    def thousandSeparator(self, n: int) -> str:

        if n == 0:
            return "0"
            
        result = ""
        countDidit = 0

        while n > 0:
            if countDidit == 3:
                result = "." + result
                countDidit = 0
            digit = n % 10
            result = str(digit) + result            
            n //= 10
            countDidit += 1

        return result