class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        N = len(spaces)
        cur_temp = []
        ans = []
        cur_idx = 0

        for i, c in enumerate(s):
            if cur_idx < N and i == spaces[cur_idx]:
                ans.append(''.join(cur_temp))
                cur_temp = []
                cur_idx += 1
            cur_temp.append(c)
        ans.append(''.join(cur_temp))
        
        return ' '.join(ans)
    

    def addSpaces(self, s: str, spaces: list[int]) -> str:
        N = len(spaces)
        idx = 0 
        ans = []

        for i in range(N):
            ans.append(s[idx: spaces[i]])
            idx = spaces[i]
        ans.append(s[idx:])
        return " ".join(ans)
    

print(Solution().addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))
print(Solution().addSpaces("icodeinpython", [1,5,7,9]))
print(Solution().addSpaces("spacing", [0,1,2,3,4,5,6]))