class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        res = 0

        for c in s:
            if c == '(':
                st.append(c)
            else:
                if st:
                    st.pop()
                else:
                    res += 1
        
        return res + len(st)
    
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        res = 0

        for c in s:
            if c == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    res += 1
        return open_count + res
    

print(Solution().minAddToMakeValid("())"))
print(Solution().minAddToMakeValid("((("))
