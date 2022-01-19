class Solution:
    def addToArrayForm(self, num: list, k: int) -> list:
        
        num[-1] += k
        
        carry = 0
        for index in range(len(num)-1, -1, -1):
            num[index] += carry
            carry = num[index] // 10
            num[index] %= 10
        
        while carry > 0:
            digit = carry % 10
            carry //= 10
            num = [digit] + num
        
        return num
        
class Solution:
    def addToArrayForm(self, num: list, k: int) -> list:
        
        num[-1] += k
        
        carry = 0
        for index in range(len(num)-1, -1, -1):
            num[index] += carry
            carry = num[index] // 10
            num[index] %= 10
        
        if carry > 0:
            num = list(map(int, str(carry))) + num
        
        return num

class Solution:
    def addToArrayForm(self, num: list, k: int) -> list:
        
        k_array = []
        
        while k > 0:
            addDigit = k % 10
            k = k // 10
            
            k_array.insert(0, addDigit)
        
        if len(num) < len(k_array):
            num, k_array = k_array, num
        
        num = num[::-1]
        k_array = k_array[::-1]
        
        index = 0
        carry = 0
        while len(num) > index or len(k_array) > index:
            d1 = 0
            d2 = 0
            if index < len(num):
                d1 = num[index]
            
            if index < len(k_array):
                d2 = k_array[index]
                
            addSum = d1 + d2 + carry
            
            carry = addSum // 10
            addSum %= 10
            
            num[index] = addSum
            
            index += 1
            
        if carry == 1:
            num.append(1)
            
        return num[::-1]