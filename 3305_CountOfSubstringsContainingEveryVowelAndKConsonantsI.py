from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        res = 0

        for idx in range(N):
            a = e = i = o = u = other = 0

            for j in range(idx, N):
                if word[j] == 'a':
                    a += 1
                elif word[j] == 'e':
                    e += 1
                elif word[j] == 'i':
                    i += 1
                elif word[j] == 'o':
                    o += 1
                elif word[j] == 'u':
                    u += 1
                else:
                    other += 1

                if a > 0 and e > 0 and i > 0 and o > 0 and u > 0 and other == k:
                    res += 1
        return res


    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        res = 0
        idx = 0
        a = e = i = o = u = other = 0

        for right in range(N):
            
            if word[right] == 'a':
                a += 1
            elif word[right] == 'e':
                e += 1
            elif word[right] == 'i':
                i += 1
            elif word[right] == 'o':
                o += 1
            elif word[right] == 'u':
                u += 1
            else:
                other += 1
            
            while idx < right and a > 0 and e > 0 and i > 0 and o > 0 and u > 0 and other != k:
                if word[idx] == 'a':
                    a -= 1
                elif word[idx] == 'e':
                    e -= 1
                elif word[idx] == 'i':
                    i -= 1
                elif word[idx] == 'o':
                    o -= 1
                elif word[idx] == 'u':
                    u -= 1
                else:
                    other -= 1
                idx += 1
            if a > 0 and e > 0 and i > 0 and o > 0 and u > 0 and other == k:
                res += 1
        return res
    

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
