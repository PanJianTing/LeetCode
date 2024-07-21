class Solution:
    def maxOperations(self, s: str) -> int:
        N = len(s)
        res = 0
        st = []
        st.append(s[0])
        cur1 = 0

        for i in range(1, N):
            if s[i] == '0':
                if st[-1] != s[i]:
                    st.append(s[i])
            else:
                st.append(s[i])

        for i in range(len(st)):
            if st[i] == '0':
                res += cur1
            else:
                cur1 += 1
        return res
    
    def maxOperations(self, s: str) -> int:
        N = len(s)
        ones = 0
        res = 0

        for i in range(N):
            if s[i] == '1':
                ones += 1
            else:
                if i > 0 and s[i-1] == '1':
                    res += ones
        return res
    
    def maxOperations(self, s: str) -> int:
        N = len(s)
        idx = 0
        ones = 0
        res = 0

        while idx < N:
            if s[idx] == '1':
                ones += 1
                idx += 1
            else:
                res += ones
                while idx < N and s[idx] == '0':
                    idx += 1
        return res
    

    def maxOperations(self, s: str) -> int:
        N = len(s)
        idx = 0
        ones = 0
        res = 0

        while idx < N:
            if s[idx] == '0':
                res += ones
                while idx < N and s[idx] == '0':
                    idx += 1
            ones += 1
            idx += 1
        return res


    

    
print(Solution().maxOperations("1001101"))
print(Solution().maxOperations("00111"))
