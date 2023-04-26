class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            n = 0
            while num > 0:
                n += num % 10
                num //= 10
            num = n
        return num
    
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        if (num % 9) == 0: return 9
        return num % 9
