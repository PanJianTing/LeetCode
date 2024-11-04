class Solution:
    def compressedString(self, word: str) -> str:
        word += "_"
        N = len(word)
        cnt = 1
        pre = word[0]
        ans = []

        for i in range(1, N):
            if word[i] == pre and cnt < 9:
                cnt += 1
            else:
                ans.append(str(cnt))
                ans.append(pre)
                pre = word[i]
                cnt = 1
        
        return ''.join(ans)
    
    def compressedString(self, word: str) -> str:
        N = len(word)
        idx = 0
        ans = []

        while idx < N:
            cur = word[idx]
            cnt = 0

            while idx < N and cnt < 9 and cur == word[idx]:
                idx += 1
                cnt += 1

            ans.append(str(cnt))
            ans.append(cur)
        
        return ''.join(ans)
            

    

print(Solution().compressedString("abcde"))
print(Solution().compressedString("aaaaaaaaaaaaaabb"))
            

