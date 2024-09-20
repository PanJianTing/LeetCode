class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        reverse = s[::-1]

        for i in range(N):
            cur_s = s[:N-i]
            check_s = reverse[i:]
            if cur_s == check_s:
                return reverse[:i] + s
        return s
    

print(Solution().shortestPalindrome("aacecaaa"))
print(Solution().shortestPalindrome("abcd"))

