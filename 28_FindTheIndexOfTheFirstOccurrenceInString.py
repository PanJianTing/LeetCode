class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(haystack) < len(needle):
        #     return -1
                
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                matchStr = haystack[i:i+len(needle)]
                if matchStr == needle:
                    return i


        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(0, n-m+1):
            for i in range(0,m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start
                
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1
        
        RADIX = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1

        for _ in range(0, m):
            MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD

        def hash_value(string: str):
            ans = 0
            factor = 1

            for i in range(m-1, -1, -1):
                ans += ((ord(string[i]) - 97) * factor) % MOD
                factor = (factor * RADIX) % MOD
            
            return ans % MOD
        
        hash_needle = hash_value(needle)

        for window_strart in range(0, (n-m+1)):
            if window_strart == 0:
                hash_hay = hash_value(haystack)
            else:
                hash_hay = ((hash_hay * RADIX) % MOD
                            - ((ord(haystack[window_strart - 1]) - 97)
                            * MAX_WEIGHT) % MOD
                            + (ord(haystack[window_strart + m - 1]) - 97) + MOD) % MOD
                
            if hash_needle == hash_hay:
                for i in range(m):
                    if needle[i] != haystack[i + window_strart]:
                        break
                    if i == m-1:
                        return window_strart
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:

        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1
        
        logest_border = [0] * m
        prev = 0
        i = 1

        while i < m:
            if needle[i] == needle[prev]:
                prev += 1
                logest_border[i] = prev
                i += 1
            else:
                if prev == 0:
                    logest_border[i] = 0
                    i += 1
                else:
                    prev = logest_border[prev - 1]

        haystack_point = 0
        needle_point = 0

        while haystack_point < n:
            if haystack[haystack_point] == needle[needle_point]:
                needle_point += 1
                haystack_point += 1

                if needle_point == m:
                    return haystack_point - m
            else:
                if needle_point == 0:
                    haystack_point += 1
                else:
                    needle_point = logest_border[needle_point - 1]

        return -1



    
# print(Solution().strStr("dbutad", "sad"))
print(Solution().strStr("a", "a"))

print(Solution().strStr("mississippi", "issip"))

