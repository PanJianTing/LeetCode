class Solution:
    def countSeniors(self, details: list[str]) -> int:
        res = 0
        for d in details:
            age = int(d[11] + d[12])
            if age > 60:
                res += 1
        return res
    

    def countSeniors(self, details: list[str]) -> int:
        res = 0
        for d in details:
            age = 10 * (ord(d[11]) - ord('0')) + (ord(d[12]) - ord('0'))

            if age > 60:
                res += 1
        return res
    

print(Solution().countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(Solution().countSeniors(["1313579440F2036","2921522980M5644"]))