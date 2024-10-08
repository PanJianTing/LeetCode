class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        st = []
        res = 0

        for i in range(N):
            cur = s[i]
            if cur == '[':
                st.append(cur)
            else:
                if st:
                    st.pop()
                else:
                    res += 1

        return (res + 1) >> 1
    

    def minSwaps(self, s: str) -> int:
        res = 0

        for c in s:
            if c == '[':
                res += 1
            else:
                if res == 0:
                    continue
                res -= 1
        
        return (res + 1) >> 1
    

print(Solution().minSwaps('][]['))
print(Solution().minSwaps(']]][[['))