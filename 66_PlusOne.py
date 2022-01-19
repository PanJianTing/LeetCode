class Solution:
    def plusOne(self, digits: list) -> list:
        lastIndex = len(digits) - 1
        carry = 0
        while lastIndex != -1:
            d = digits[lastIndex]
            d += 1
            carry = d // 10
            d = d % 10
            digits[lastIndex] = d
            lastIndex -= 1
            if carry == 0:
                return digits
        
        return [1] + digits