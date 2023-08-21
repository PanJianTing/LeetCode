class Solution:
    def encode(self, strs) -> str:
        res = ""
        for s in strs:
            res += s
            res += "π"

        return res
    
    def decode(self, s) -> list[str]:
        return s.split("π")[:-1]


class Solution:
    def encode(self, strs) -> str:
        # res = ""
        # for s in strs:
        #     res += s
        #     res += "π"

        return "π".join(strs)
    
    def decode(self, s) -> list[str]:
        return s.split("π")

class Solution:
    def encode(self, strs) -> str:

        res = ""
        for s in strs:
            if "/" in s:
                res += s.replace("/", "//") 
            else:
                res += s
            res += "/:"
        
        return res
    
    def decode(self, s) -> list[str]:

        tempS = ""
        res = []
        idx = 0
        N = len(s) - 1
        while idx < N:
            tempC = s[idx]

            if "/" == tempC:
                if ":" == s[idx+1]:
                    res.append(tempS)
                    tempS = ""
                    idx += 1
                else:
                    tempS += "/"
                    idx += 1
            else:
                tempS += tempC

            idx += 1
        
        return res
    
# print(Solution().decode(Solution().encode(["Hello", "World", "Nice", "To", "Meet", "You"])))
print(Solution().decode(Solution().encode(["Hello", "Wor/:ld", "Nice", "To", "Meet", "You"])))
print(Solution().decode(Solution().encode(["Hello", "Wor/:ld", "Nice", "To", "Me/et", "You"])))


                
                