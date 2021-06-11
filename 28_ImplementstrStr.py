class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == needle or needle == "":
            return 0

        if needle not in haystack:
            return -1

        for i in range(len(haystack)):

            if haystack[i] == needle[0]:
                check = haystack[i:i+len(needle)]
                if check == needle:
                    return i


        return -1


Solution.strStr(Solution(), "", "")
Solution.strStr(Solution(), "hello", "ll")