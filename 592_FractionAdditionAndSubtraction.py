class Solution:
    def fractionAddition(self, E: str) -> str:
        N = len(E)
        symbol = set(['/', '+', '-'])
        idx = 0
        mul = 1
        up = []
        down = []
        isPositive = 1
        res = 0

        while idx < N:
            if E[idx] == '/':
                idx += 1
                temp = ""
                while idx < N and E[idx] not in symbol:
                    temp += E[idx]
                    idx += 1
                down.append(int(temp))
                mul *= down[-1]
            elif E[idx] == "+":
                isPositive = 1
                idx += 1
            elif E[idx] == "-":
                isPositive = -1
                idx += 1
            else:
                temp = ""
                while idx < N and E[idx] not in symbol:
                    temp += E[idx]
                    idx += 1
                up.append(isPositive * int(temp))
            

        for c, m in zip(up, down):
            res += (mul // m) * c

        if res == 0 or res % mul == 0:
            return str(res // mul) + '/1'


        for i in range(abs(res), 0, -1):
            if mul % i == 0 and res % i == 0:
                mul //= i
                res //= i
                break
        
        return str(res) + '/' + str(mul)
    


    def fractionAddition(self, E: str) -> str:
        N = len(E)
        symbol = set(['+', '/', '-'])
        idx = 0
        up = 0
        down = 1
        
        def findGCD(a, b):
            if a == 0:
                return b
            return findGCD(b % a, a)

        while idx < N:
            
            positive = 1
            # check sign
            if E[idx] == "-":
                positive = -1
                idx += 1
            elif E[idx] == "+":
                positive = 1
                idx += 1
            
            temp_up = 0
            mul = 1
            while idx < N and E[idx] not in symbol:
                temp_up = temp_up * mul + int(E[idx])
                mul *= 10
                idx += 1
            
            temp_up *= positive
            idx += 1

            temp_down = 0
            mul = 1
            while idx < N and E[idx] not in symbol:
                temp_down = temp_down * mul + int(E[idx])
                mul *= 10
                idx += 1

            up = up * temp_down + temp_up * down
            down *= temp_down

        gcd = findGCD(abs(up), abs(down))

        return f"{up // gcd}/{down // gcd}"
    

print(Solution().fractionAddition("1/3-1/2"))
print(Solution().fractionAddition("-5/2+10/3+7/9"))

