from collections import defaultdict

class Solution:
    
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        vowel = ('a', 'e', 'i', 'o', 'u')

        def count(m):
            vowel_map = defaultdict(int)
            consonants = 0
            ans = 0
            l = 0
            r = 0
            while r < N or l < N:
                if len(vowel_map) == 5 and consonants >= m:
                    ans += N - r + 1
                    if word[l] not in vowel:
                        consonants -= 1
                    else:
                        vowel_map[word[l]] -= 1
                        if vowel_map[word[l]] == 0:
                            del vowel_map[word[l]]
                    l += 1
                else:
                    if r == N:
                        break
                    if word[r] not in vowel:
                        consonants += 1
                    else:
                        vowel_map[word[r]] += 1
                    r += 1
            return ans
        return count(k) - count(k+1)



print(Solution().countOfSubstrings("aeioqq", 1))    
print(Solution().countOfSubstrings("aeiou", 0))    
print(Solution().countOfSubstrings("ieaouqqieaouqq", 1))    
