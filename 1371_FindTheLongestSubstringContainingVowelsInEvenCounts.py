class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        charMap = [0] * 26
        mp = [-1] * 32
        res = 0

        charMap[ord('a') - ord('a')] = 1
        charMap[ord('e') - ord('a')] = 2
        charMap[ord('i') - ord('a')] = 4
        charMap[ord('o') - ord('a')] = 8
        charMap[ord('u') - ord('a')] = 16

        for i, c in enumerate(s):
            prefixXOR ^= charMap[ord(c) - ord('a')]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            res = max(res, i - mp[prefixXOR])

        return res


print(Solution().findTheLongestSubstring('eleetminicoworoep'))