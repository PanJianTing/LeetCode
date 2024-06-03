class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        M = len(s)
        N = len(t)
        ps = 0
        pt = 0

        while ps < M and pt < N:
            if s[ps] == t[pt]:
                pt += 1
            ps += 1
        
        return N - pt
    
print(Solution().appendCharacters("coaching", "coding"))
print(Solution().appendCharacters("abcde", "a"))
print(Solution().appendCharacters("z", "abcde"))
