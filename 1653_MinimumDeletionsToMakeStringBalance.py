class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        a_count_list = [0] * N
        b_count_list = [0] * N
        a_count = 0
        b_count = 0
        res = N

        for i in range(N):
            b_count_list[i] = b_count
            if s[i] == 'b':
                b_count += 1
        
        for i in range(N-1, -1, -1):
            a_count_list[i] = a_count
            if s[i] == 'a':
                a_count += 1

        for i in range(N):
            res = min(res, a_count_list[i] + b_count_list[i])

        return res
    
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        a_counts = [0] * N
        a_count = 0
        b_count = 0
        res = N

        for i in range(N-1, -1, -1):
            a_counts[i] = a_count
            if s[i] == 'a':
                a_count += 1
        
        for i in range(N):
            res = min(res, a_counts[i] + b_count)
            if s[i] == 'b':
                b_count += 1

        return res
    
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        a_count = s.count('a')
        b_count = 0
        res = N
        
        for i in range(N):
            if s[i] == 'a':
                a_count -= 1
            res = min(res, a_count + b_count)
            if s[i] == 'b':
                b_count += 1

        return res
    
    def minimumDeletions(self, s: str) -> int:
        st = []
        res = 0

        for c in s:
            if st and st[-1] == 'b' and c == 'a':
                st.pop()
                res += 1
            else:
                st.append(c)
        return res
    
    def minimumDeletions(self, s: str) -> int:
        res = 0
        b_count = 0

        for c in s:
            if c == 'b':
                b_count += 1
            elif b_count > 0:
                res += 1
                b_count -= 1
            
        return res

print(Solution().minimumDeletions('ababaaaabbbbbaaa'))
print(Solution().minimumDeletions('aababbab'))
print(Solution().minimumDeletions('bbaaaaabb'))


        