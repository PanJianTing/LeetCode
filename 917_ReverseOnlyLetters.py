class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letterIndex = []

        for i, c in enumerate(s):
            if c.isalpha():
                letterIndex.append(i)
        
        s = list(s)
        n = len(letterIndex)//2

        for i in zip(letterIndex[:n], letterIndex[::-1][:n]):
            s[i[0]], s[i[1]] = s[i[1]], s[i[0]]

        return "".join(s)

    def reverseOnlyLetters_my(self, s: str) -> str:
        
        letters = []

        result = []

        for c in s:
            
            if c.isalpha():
                letters.append(c)
                result.append("\\")
            else:
                result.append(c)

        ans = ""
        for c in result:

            if c == "\\":
                ans += letters.pop()
            else:
                ans += c

        return ans


Solution.reverseOnlyLetters(Solution(), "Test1ng-Leet=code-Q!")