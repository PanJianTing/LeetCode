class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)
        num = 0
        res = 0
        cur = 1

        for i in range(N-1, -1, -1):
            num += int(s[i]) * cur
            cur <<= 1
        
        while num > 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            res += 1

        return res
    
    def numSteps(self, s: str) -> int:
        res = 0
        s = list(s)

        while not (len(s) == 1 and s[0] == '1'):
            N = len(s)

            if s[-1] == "1":
                is_add = False
                for i in range(N-1, -1, -1):
                    if s[i] == '0':
                        s[i] = '1'
                        is_add = True
                        break
                    else:
                        s[i] = '0'

                if is_add == False:
                    s = ['1'] + s
                    
                pass
            else:
                s.pop()
            res += 1
        return res
    
    def numSteps(self, s: str) -> int:
        N = len(s)
        res = 0
        carry = 0

        for i in range(N-1, 0, -1):
            temp = int(s[i]) + carry

            if temp & 1:
                res += 2
                carry = 1
            else:
                res += 1
        return res + carry

print(Solution().numSteps("1101"))
print(Solution().numSteps("10"))
print(Solution().numSteps("1"))
print(Solution().numSteps("10"))
print(Solution().numSteps("1001"))