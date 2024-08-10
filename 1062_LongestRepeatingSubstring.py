class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        N = len(s)
        max_l = N-1

        for i in range(max_l, 0, -1):
            check_set = set()
            j = 0
            while j + i <= N:
                cur = s[j:j+i]
                if cur in check_set:
                    return i
                check_set.add(cur)
                j += 1
        return 0


print(Solution().longestRepeatingSubstring("abcd"))
print(Solution().longestRepeatingSubstring("abbaba"))
print(Solution().longestRepeatingSubstring("aabcaabdaab"))
print(Solution().longestRepeatingSubstring("aaaaa"))