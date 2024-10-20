class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        oper_st = []
        cur_operation = ''

        for c in expression:
            if c == '(':
                st.append('(')
            elif c == ')':
                cur_operation = oper_st.pop()
                temp = True if 't' == st.pop() else False
                if cur_operation == '!':
                    temp = not temp
                    st.pop()
                else:
                    while st:
                        cur_c = st.pop()
                        if cur_c == '(':
                            break
                        cur_bool = True if 't' == cur_c else False
                        if cur_operation == '&':
                            temp &= cur_bool
                        else:
                            temp |= cur_bool
                st.append('t') if temp else st.append('f')

            elif c == '&' or c == '|' or c == '!':
                oper_st.append(c)
            elif c == 'f' or c == 't':
                st.append(c)

        return True if 't' == st.pop() else False
    

# print(Solution().parseBoolExpr('&(|(f))'))
# print(Solution().parseBoolExpr('|(f,f,f,t)'))
# print(Solution().parseBoolExpr('!(&(f,t))'))
# print(Solution().parseBoolExpr('|(f,&(t,t))'))
print(Solution().parseBoolExpr('!(&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))))'))

            
