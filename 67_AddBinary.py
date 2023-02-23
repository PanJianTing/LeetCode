from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        x = int(a, 2)
        y = int(b, 2)
        
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            print(ans, carry)
            
            x, y = ans, carry
            
        return bin(x)[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        total = []
        carry = 0
        index = 0
        while len(a) > index or len(b) > index:
            b1 = 0
            b2 = 0
            if index < len(a):
                b1 = a[index]
            if index < len(b):
                b2 = b[index]
            
            addSum = int(b1) + int(b2) + carry
            
            carry = addSum // 2
            addSum %= 2
            
            total.append(addSum)
            index += 1
        if carry == 1:
            total.append(1)
        
        print(total)
        return "".join(str(s) for s in reversed(total))
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        aList = list(a)[::-1]
        bList = list(b)[::-1]

        res = list()
        carry = "0"

        for i, j in zip_longest(aList, bList):

            next = "0"
            if i == None:
                i = "0"
            if j == None:
                j = "0"
            
            if i != j:
                next = "1"
            
            if carry != next:
                next = "1"
                if i == "1" and j == "1":
                    carry = "1"
                else:
                    carry = "0"
            else:
                next = "0"
                if i == "1" or j == "1":
                    carry = "1"
                else:
                    carry = "0"
                

            res.append(next)

        if carry == "1":
            res.append(carry)
        return "".join(res[::-1])

    def addBinary(self, a: str, b: str) -> str:

        return '{0:b}'.format(int(a,2)+int(b,2))

    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []

        for i in range(n-1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            
            if carry % 2:
                ans.append("1")
            else:
                ans.append("0")
            
            carry //= 2
        
        if carry:
            ans.append("1")

        return "".join(ans[::-1])

    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]
        
print(Solution().addBinary("111", "11"))