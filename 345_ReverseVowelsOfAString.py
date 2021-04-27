class Solution:
    def reverseVowels(self, s: str) -> str:
        
        defVowels = "aeiouAEIOU"
        listS = list(s)
        left = 0
        right = len(listS) - 1
        
        while left < right:
            if listS[left] in defVowels and listS[right] in defVowels:
                
                listS[left], listS[right] = listS[right], listS[left]
                
                left += 1
                right -= 1
            elif listS[left] not in defVowels:
                left += 1
            
            elif listS[right] not in defVowels:
                right -= 1
            
        return "".join(listS)



    def reverseVowels_my(self, s: str) -> str:
        
        defVowels = ['a', "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowels = []
        result = ""
        
        for c in s:
            if c in defVowels:
                vowels.append(c)
                
        for i in range(len(s)):
            if s[i] in defVowels:
                result += vowels.pop()
            else:
                result += s[i]

        return result
    
    
print(Solution().reverseVowels("hello"))