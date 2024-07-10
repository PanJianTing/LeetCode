class Solution:
    def minOperations(self, logs: list[str]) -> int:
        N = len(logs)
        res = 0

        for i in range(N):
            cur = logs[i]
            if '../' == cur:
                if res:
                    res -= 1
            elif './' == cur:
                continue
            else:
                res += 1
        return res
    
    def minOperations(self, logs: list[str]) -> int:
        st = []

        for log in logs:
            if '../' == log:
                if st:
                    st.pop()
            elif './' == log:
                continue
            else:
                st.append(log)
        
        return len(st)
    
print(Solution().minOperations(["d1/","d2/","../","d21/","./"]))
        