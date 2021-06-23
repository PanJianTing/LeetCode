class Solution:
    def modifyString(self, s: str) -> str:

        s = list("/" + s + "/")

        for i in range(1, len(s) - 1):
            if s[i] == "?":
                for alpha in "abc":
                    if s[i-1] != alpha and s[i+1] != alpha:
                        s[i] = alpha
                        break
        return "".join(s[1:-1])


    def modifyString_my(self, s: str) -> str:

        s = list(s)

        alphaList = ["a", "b", "c"]

        for i in range(0, len(s)):
            if s[i] == '?':
                for alpha in alphaList:
                    isOK = True
                    if i - 1 > -1:
                        if alpha == s[i-1]:
                            isOK = False
                    
                    if i + 1 < len(s):
                        if alpha == s[i+1]:
                            isOK = False
                    
                    if isOK:
                        s[i] = alpha
                        break

        return "".join(s)


Solution.modifyString(Solution(), "??yw?ipkj?")