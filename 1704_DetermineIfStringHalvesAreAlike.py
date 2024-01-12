class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        a_idx = 0
        a_cnt = 0
        b_cnt = 0
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        for b_idx in range(N >> 1, N):
            if s[a_idx] in vowel_set:
                a_cnt += 1
            if s[b_idx] in vowel_set:
                b_cnt += 1
            
            a_idx += 1
        
        return a_cnt == b_cnt
    
    def halvesAreAlike(self, s) -> bool:
        N = len(s)

        def countVowel(st, end):
            vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
            cnt = 0

            for i in range(st, end):
                if s[i] in vowel_set:
                    cnt += 1
            return cnt
        return countVowel(0, N>>1) == countVowel(N>>1, N)
    

print(Solution().halvesAreAlike("book"))
print(Solution().halvesAreAlike("textbook"))
