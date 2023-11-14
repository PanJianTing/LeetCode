from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s) -> int:

        cntMap = defaultdict(list)

        for i, c in enumerate(s):
            cntMap[c].append(i)
        
        ans = 0

        # if to same char have other same char is wrong
        # example 'abba' is wrong
        for key in cntMap.keys():
            if len(cntMap[key]) > 1:
                idx = cntMap[key]
                ans += (idx[-1] - idx[0] - 1)
                if len(idx) > 3:
                    ans -= (len(idx) - 2)
                    ans += 1
        
        return ans
    
    def countPalindromicSubsequence(self, s) -> int:

        cntMap = defaultdict(list)

        for i, c in enumerate(s):
            cntMap[c].append(i)
        
        ans = 0

        for key in cntMap.keys():
            idx = cntMap[key]
            if len(idx) > 1:
                ans += len(set(s[idx[0]+1 : idx[-1]]))
        
        return ans
    
    def countPalindromicSubsequence(self, s) -> int:

        ans = 0
        letters = set(s)

        for l in letters:
            i, j = s.index(l), s.rindex(l)

            if i == j:
                continue

            ans += len(set(s[i+1 : j]))
        
        return ans
    
    def countPalindromicSubsequence(sefl, s) -> int:
        ans = 0
        first = [-1] * 26
        last = [-1] * 26
        
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        for i in range(26):
            if first[i] == -1:
                continue
                
            ans += len(set(s[first[i]+1 : last[i]]))

        return ans

print(Solution().countPalindromicSubsequence('tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp'))
print(Solution().countPalindromicSubsequence('bbcbaba'))
print(Solution().countPalindromicSubsequence('adc'))
print(Solution().countPalindromicSubsequence('aabca'))
print(Solution().countPalindromicSubsequence('abba'))