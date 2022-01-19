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
        
print(Solution().addBinary("111", "11"))