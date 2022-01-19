class Solution:
    def addStrings(self, a: str, b: str) -> str:
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
            
            carry = addSum // 10
            addSum %= 10
            
            total.append(addSum)
            index += 1
        if carry == 1:
            total.append(1)
        
        # print(total)
        return "".join(str(s) for s in reversed(total))
        
print(Solution().addStrings("11", "123"))