class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""

        for c in s:
            if c == '*':
                ans = ans[:-1]
            else:
                ans += c
        
        return ans
    
    def removeStars(self, s: str) -> str:

        stack = []

        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)