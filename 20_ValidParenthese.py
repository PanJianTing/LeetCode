class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif stack:
                openBracket = stack.pop()
                if openBracket == '(':
                    if c == ')':
                        continue
                    else:
                        return False
                elif openBracket == '[':
                    if c == ']':
                        continue
                    else:
                        return False
                    
                elif openBracket == '{':
                    if c == '}':
                        continue
                    else:
                        return False
            else:
                return False
        

        return True if len(stack) == 0 else False
    

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {'[':']', '{':'}', '(':')'}

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif stack:
                openBracket = stack.pop()

                if openBracket in mapping:
                    if mapping[openBracket] == c:
                        continue
                    else:
                        return False
            else:
                return False
        

        return True if len(stack) == 0 else False
    

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {']':'[', '}':'{', ')':'('}

        for c in s:
            if c in mapping:

                top = stack.pop() if stack else '#'

                if mapping[c] == top:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False
                

                