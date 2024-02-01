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


print(int(6/-132))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))