class Solution:
    def minLength(self, s: str) -> int:

        while "AB" in s or "CD" in s:

            N = len(s)
            temp = []
            idx = 0

            while idx < N:
                if idx+1 < N and ((s[idx] == "A" and s[idx+1] == "B") or (s[idx] == "C" and s[idx+1] == "D")):
                    idx += 1
                else:
                    temp.append(s[idx])
                idx += 1
            s = "".join(temp)

        return len(s)
    
    def minLength(self, s: str) -> int:
        N = len(s)
        st = []

        for i in range(N):
            if st and ((st[-1] == "A" and s[i] == "B") or (st[-1] == "C" and s[i] == "D")):
                st.pop()
            else:
                st.append(s[i])
        return len(st)
    
    def minLength(self, s: str) -> int:
        
        while "AB" in s or "CD" in s:
            s = s.replace('AB', "")
            s = s.replace('CD', "")

        return len(s)
    
    def minLength(self, s: str) -> int:
        s = list(s)
        write_ptr = 0

        for read_ptr in range(len(s)):
            s[write_ptr] = s[read_ptr]

            if write_ptr > 0 and ((s[write_ptr-1] == "A" and s[write_ptr] == "B") or (s[write_ptr-1] == "C" and s[write_ptr] == "D")):
                write_ptr -= 1
            else:
                write_ptr += 1
        
        return write_ptr
        

    

print(Solution().minLength("ABFCACDB"))
print(Solution().minLength("ACBBD"))

        