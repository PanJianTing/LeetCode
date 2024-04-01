class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        N = len(s)
        res = 0

        for i in range(N):
            if s[i] == ' ':
                res = 0
            else:
                res += 1
        return res
    
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        res = 0
        meet_char = False

        for i in range(N-1, -1, -1):
            if s[i] == " ":
                if meet_char:
                    return res
            else:
                meet_char = True
                res += 1
        return res
    
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        cur_idx = N-1
        res = 0
        
        # trim trailing
        while cur_idx >= 0 and s[cur_idx] == ' ':
            cur_idx -= 1
        
        # find word length
        while cur_idx >= 0 and s[cur_idx] != ' ':
            res += 1
            cur_idx -= 1

        return res
    
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        cur_idx = N-1
        res = 0

        while cur_idx > -1:
            if s[cur_idx] == ' ':
                if res > 0:
                    return res
            else:
                res += 1
            cur_idx -= 1
        return res


                

print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
print(Solution().lengthOfLastWord("luffy is still joyboy"))