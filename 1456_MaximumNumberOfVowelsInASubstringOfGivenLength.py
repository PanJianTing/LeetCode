class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vowelSet = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(0, k):
            if s[i] in vowelSet:
                ans += 1
        
        now = ans
        for i in range(k, len(s)):
            # print(start, end)
            if s[i] in vowelSet:
                now += 1
            if s[i-k] in vowelSet:
                now -= 1
            
            ans = max(ans, now)

        return ans
    
    def maxVowels(self, s: str, k: int) -> int:
        vowelSet = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0
        L = len(s)
        now = 0
        for i in range(0, L):
            now += 1 if s[i] in vowelSet else 0
            if i >= k:
                now -=  1 if s[i-k] in vowelSet else 0
            ans = max(ans, now)
        
        return ans

    
print(Solution().maxVowels('abciiidef', 3))
                
        