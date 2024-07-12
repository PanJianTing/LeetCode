class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        N = len(s)
        res = 0
        st = []
        st2 = []
        add1 = x
        add2 = y
        first = 'a'
        second = 'b'
        if y > x:
            first = 'b'
            second = 'a'
            add1 = y
            add2 = x

        for i in range(N):
            cur_c = s[i]
            if st:
                if cur_c == second and st[-1] == first:
                    st.pop()
                    res += add1
                else:
                    st.append(cur_c)
            else:
                st.append(cur_c)


        for i in range(len(st)):
            cur_c = st[i]
            if st2:
                if cur_c == first and st2[-1] == second:
                        st2.pop()
                        res += add2
                else:
                    st2.append(cur_c)
            else:
                st2.append(cur_c)

        return res
    

    def maximumGain(self, s: str, x: int, y: int) -> int:
        N = len(s)
        res = 0
        high_str = 'ab'
        low_str = 'ba'
        if y > x:
            high_str = 'ba'
            low_str = 'ab'
        
        def removeStr(cur_s, cur_remove):
            st = []

            for i in range(len(cur_s)):
                cur_c = cur_s[i]
                if st and cur_c == cur_remove[1] and st[-1] == cur_remove[0]:
                    st.pop()
                else:
                    st.append(cur_c)
            return ''.join(st)

        afterRemoveHigh = removeStr(s, high_str)
        res += max(x, y) * ((N - len(afterRemoveHigh)) // 2)
        afterRemoveLow = removeStr(afterRemoveHigh, low_str)
        res += min(x, y) * ((len(afterRemoveHigh) - len(afterRemoveLow)) // 2)

        return res
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        s = list(s)

        def removeStr(cur_s, cur_remove, point):
            total_point = 0
            write_idx = 0
            N = len(cur_s)
            for read_idx in range(N):
                cur_s[write_idx] = cur_s[read_idx]

                if write_idx > 0 and cur_s[write_idx-1] == cur_remove[0] and cur_s[write_idx] == cur_remove[1]:
                    write_idx -= 2
                    total_point += point
                write_idx += 1
            cur_s = cur_s[:write_idx]
        
            return cur_s, total_point
        
        if x > y:
            s, res1 = removeStr(s, 'ab', x)
            s, res2 = removeStr(s, 'ba', y)
            res = res1 + res2
        else:
            s, res1 = removeStr(s, 'ba', y)
            s, res2 = removeStr(s, 'ab', x)
            res = res1 + res2
        
        return res
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        N = len(s)
        res = 0
        a_cnt = 0
        b_cnt = 0
        first = 'a'
        second = 'b' 
        if y > x:
            x, y = y, x
            first, second = second, first

        for i in range(N):
            cur_c = s[i]
            if cur_c == second:
                if a_cnt > 0:
                    a_cnt -= 1
                    res += x
                else:
                    b_cnt += 1
            elif cur_c == first:
                a_cnt += 1
            else:
                res += min(a_cnt, b_cnt) * y
                a_cnt = 0
                b_cnt = 0
        res += (min(a_cnt, b_cnt) * y)
        return res

    
print(Solution().maximumGain('cdbcbbaaabab', 4, 5))
print(Solution().maximumGain('aabbaaxybbaabb', 5, 4))