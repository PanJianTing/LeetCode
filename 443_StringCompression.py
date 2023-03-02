from collections import defaultdict

class Solution:
    def compress(self, chars: list[str]) -> int:

        chars.append("")
        start = 0
        countEnd = 0

        for i in range(0, len(chars)):
            if chars[start] != chars[i]:
                count = i - start
                chars[countEnd] = chars[start]
                countEnd += 1
                if count > 1:
                    for c in str(count):
                        chars[countEnd] = c

                start = i

        return countEnd

    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while i + group_length < len(chars) and chars[i] == chars[i+group_length]:
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                count_str = str(group_length)
                chars[res: res+len(count_str)] = list(count_str)
                res += len(count_str)
            i += group_length
        return res
    
# print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    
