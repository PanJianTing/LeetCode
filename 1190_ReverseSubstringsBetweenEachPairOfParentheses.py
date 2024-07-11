class Solution:
    def reverseParentheses(self, s: str) -> str:
        N = len(s)
        st1 = []
        st2 = []

        for i in range(N):
            cur_c = s[i]
            if cur_c == ')':
                while st1 and st1[-1] != '(':
                    st2.append(st1.pop())
                st1.pop()
                while st2:
                    st1.append(st2.pop(0))
            else:
                st1.append(cur_c)
        return ''.join(st1)

    def reverseParentheses(self, s: str) -> str:
        N = len(s)
        open_idx = []
        res = []

        for i in range(N):
            cur_c = s[i]
            if cur_c == "(":
                open_idx.append(len(res))
            elif cur_c == ")":
                st = open_idx.pop()
                res[st:] = res[st:][::-1]
            else:
                res.append(cur_c)

        return ''.join(res)
    

    def reverseParentheses(self, s: str) -> str:
        N = len(s)
        open_idx = []
        pair = [0] * N
        res = []
        cur_idx = 0
        direction = 1

        for i in range(N):
            cur_c = s[i]
            if cur_c == '(':
                open_idx.append(i)
            elif cur_c == ')':
                j = open_idx.pop()
                pair[i] = j
                pair[j] = i

        while cur_idx < N:
            if s[cur_idx] == '(' or s[cur_idx] == ')':
                cur_idx = pair[cur_idx]
                direction = -direction
            else:
                res.append(s[cur_idx])
            cur_idx += direction
        
        return ''.join(res)
        
                
    
    
    

# print(Solution().reverseParentheses("(abcd)"))
# print(Solution().reverseParentheses("(u(love)i)"))
print(Solution().reverseParentheses("(ed(et(oc))el)"))