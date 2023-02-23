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
    
from itertools import zip_longest

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        num = num[::-1]
        ks = []

        while k > 0:
            ks.append(k%10)
            k = k // 10

        print(ks, num)

        res = []

        carry = 0
        for i, j in zip_longest(num, ks):
            if i == None:
                i = 0
            if j == None:
                j = 0

            add = i + j + carry

            carry = add // 10
            res.append(add % 10)
        
        if carry == 1:
            res.append(carry)
        return res[::-1]

    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        # carry = 0
        for i in range(len(num) - 1, -1, -1):
            add = num[i] + k
            num[i] = add % 10
            k = add // 10

        if k > 0:
            num = list(map(int, str(k))) + num
            

        return num

    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        num[-1] += k
        for i in range(len(num) - 1, -1, -1):
            carry, num[i] = divmod(num[i], 10)
            if i:
                num[i-1] += carry

        if carry:
            num = list(map(int, str(carry))) + num

        return num