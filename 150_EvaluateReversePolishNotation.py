class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        notation = set(["+", "-", "*", "/"])

        for t in tokens:
            if t in notation:
                pop1 = st.pop()
                pop2 = st.pop()
                newPush = 0
                if t == "+":
                    newPush = pop2 + pop1
                elif t == "-":
                    newPush = pop2 - pop1
                elif t == "*":
                    newPush = pop2 * pop1
                elif t == '/':
                    newPush = int(pop2 / pop1)
                st.append(newPush)
            else:
                st.append(int(t))
        
        return st[-1]
    
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+" : lambda a, b : a+b,
            "-" : lambda a, b : a-b,
            "*" : lambda a, b : a*b,
            "/" : lambda a, b : int(a/b)
        }
        cur_num = 0
        idx = 0

        while len(tokens) > 1:
            cur_notation = tokens[idx]
            if tokens[idx] in operations:
                num1 = int(tokens[cur_num-1])
                num2 = int(tokens[cur_num])
                num = operations[cur_notation](num1, num2)
                tokens.pop(cur_num-1)
                tokens.pop(cur_num-1)
                tokens[cur_num-1] = str(num)
                idx = cur_num - 1
                cur_num -= 1
            else:
                cur_num = idx
            idx += 1
        return int(tokens[0])
    

    def evalRPN(self, tokens: list[str]) -> int:

        operations = {
            "+" : lambda a, b : a+b,
            "-" : lambda a, b : a-b,
            "*" : lambda a, b : a*b,
            "/" : lambda a, b : int(a/b),
        }

        cur_idx = 0

        while len(tokens) > 1:

            while tokens[cur_idx] not in operations:
                cur_idx += 1
            
            num1 = int(tokens[cur_idx-2])
            num2 = int(tokens[cur_idx-1])
            num = operations[tokens[cur_idx]](num1, num2)
            tokens[cur_idx] = num
            
            tokens.pop(cur_idx-2)
            tokens.pop(cur_idx-2)
            cur_idx -= 1

        return int(tokens[0])
    
    def evalRPN(self, tokens: list[str]) -> int:

        st = []
        operations = {
            "+" : lambda a, b: a+b,
            "-" : lambda a, b: a-b,
            "*" : lambda a, b: a*b,
            "/" : lambda a, b: int(a/b)
        }

        for t in tokens:
            if t in operations:
                num2 = st.pop()
                num1 = st.pop()

                st.append(operations[t](num1, num2))
            else:
                st.append(int(t))

        return st[0]
            
# print(int(6/-132))
print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))