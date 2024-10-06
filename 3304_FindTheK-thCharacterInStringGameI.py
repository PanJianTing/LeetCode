class Solution:
    def kthCharacter(self, k: int) -> str:
        cur_str = 'a'
        
        while len(cur_str) < k:

            temp = ''

            for c in cur_str:
                if c == 'z':
                    temp += (c + 'a')
                else:
                    temp += c + chr(ord(c) + 1)
            cur_str = temp
        
        return cur_str[k-1]
    
print(Solution().kthCharacter(5))
        