class Solution:
    def parseTernary(self, expression) -> str:
        s1 = []
        s2 = []

        for s in expression:
            if s == "?" or s == ":":
                s1.append(s)
            else:
                s2.append(s)
        
        res = ""
        while s1:
            now = s1.pop()

            if now == ":":
                if ":" in res:
                    res = s2.pop() + ':' + res
                else:
                    res = s2.pop()
                    res = s2.pop() + ":" + res
            else:
                condition = s2.pop()
                if condition == "T":
                    res = res.split(':')[0]
                else:
                    res = res.split(':')[1]
                s2.append(res)

        return res

# print(Solution().parseTernary("T?2:3"))
# print(Solution().parseTernary("F?1:T?4:5"))
print(Solution().parseTernary("T?T?F:5:3"))
