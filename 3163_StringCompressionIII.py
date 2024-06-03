class Solution:
    def compressedString(self, word: str) -> str:
        word = word + "."
        N = len(word)
        res = ""
        pre = ""
        cnt = 0

        for i in range(N):
            if pre == word[i] and cnt < 9:
                cnt += 1
            else:
                if pre != "":
                    res += (str(cnt) + pre)
                pre = word[i]
                cnt = 1

        return res
    
print(Solution().compressedString('abcde'))
print(Solution().compressedString('aaaaaaaaaaaaaabb'))

            

