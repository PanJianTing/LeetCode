class Solution:
    def convertToTitle(self, num):
        res = ""
        base = ord('A') - 1
        while num > 26:
            curr = num % 26
            num = num //  26
            if curr == 0:
                curr = 26
                num -= 1
            res += chr(curr+base)

        # print(num)
        if num > 0:
            res +=  chr(num+base)
        
        return res[::-1]
    
    def convertToTitle(self, num):
        res = ""
        base = ord('A') - 1
        while num > 26:
            curr = num % 26
            num = num //  26
            if curr == 0:
                curr = 26
                num -= 1
            res = chr(curr+base) + res

        # print(num)
        if num > 0:
            res = chr(num+base) + res
        
        return res
    
    def convertToTitle(self, num):

        res = ""
        base = ord("A")
        
        while num > 0:
            num -= 1
            curr = (num) % 26
            num //= 26
            res = chr(curr + base) + res
        return res


    def convertToTitle(self, num):
        res = ""
        base = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        while num > 0:
            num -= 1
            curr = (num) % 26
            num //= 26
            res = base[curr] + res
        return res
    

print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
print(Solution().convertToTitle(2147483647))
print(Solution().convertToTitle(52))
print(Solution().convertToTitle(51))