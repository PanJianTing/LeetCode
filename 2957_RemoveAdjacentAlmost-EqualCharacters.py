class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        N = len(word)
        i = 1

        while i < N:
            if abs(ord(word[i]) - ord(word[i-1])) < 2:
                ans += 1
                i += 1
            i += 1
        
        return ans
    
print(Solution().removeAlmostEqualCharacters("ca"))
print(Solution().removeAlmostEqualCharacters("aaaaa"))
print(Solution().removeAlmostEqualCharacters("abddez"))
print(Solution().removeAlmostEqualCharacters("zyxyxyz"))
print(Solution().removeAlmostEqualCharacters("acb"))
print(Solution().removeAlmostEqualCharacters("acba"))