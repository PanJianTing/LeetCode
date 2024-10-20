class Solution:
    def stringSequence(self, target: str) -> list[str]:
        N = len(target)
        ans = []
        cur_idx = 0
        cur = ''

        while cur_idx < N:
            if cur == '':
                cur += 'a'
            else:
                if cur[-1] == target[cur_idx]:
                    cur_idx += 1
                    if cur_idx == N:
                        break
                    cur += 'a'
                else:
                    temp = cur[-1]
                    cur = cur[:-1] + chr(ord(temp) + 1)
                
            ans.append(cur)
        
        return ans
    
    def stringSequence(self, target: str) -> list[str]:
        ans = []
        cur = ''

        for c in target:
            cur += 'a'
            ans.append(cur)

            while cur[-1] != c:
                cur = cur[:-1] + (chr(ord(cur[-1]) + 1) if cur[-1] != 'z' else 'a')
                ans.append(cur)
        
        return ans



print(Solution().stringSequence('abc'))
print(Solution().stringSequence('he'))
        
