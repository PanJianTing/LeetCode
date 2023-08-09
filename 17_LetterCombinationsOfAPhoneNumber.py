from collections import defaultdict

class Solution:
    def letterCombinations(self, digit) -> list[str]:

        if not digit:
            return []
        digitMap = defaultdict(list)

        digitMap["2"] = ["a", "b", "c"]
        digitMap["3"] = ["d", "e", "f"]
        digitMap["4"] = ["g", "h", "i"]
        digitMap["5"] = ["j", "k", "l"]
        digitMap["6"] = ["m", "n", "o"]
        digitMap["7"] = ["p", "q", "r", "s"]
        digitMap["8"] = ["t", "u", "v"]
        digitMap["9"] = ["w", "x", "y", "z"]

        ans = []
        def backtrack(d, curr):
            if len(d) == 0:
                ans.append(curr)
                return
            
            for c in digitMap[d[0]]:
                backtrack(d[1:], curr + c)
                
        backtrack(digit, "")
        return ans
    
    def letterCombinations(self, digit) -> list[str]:
        if digit == "":
            return []
        ans = [""]
        digit = list(digit)

        digitMap = defaultdict(list)
        digitMap["2"] = ["a", "b", "c"]
        digitMap["3"] = ["d", "e", "f"]
        digitMap["4"] = ["g", "h", "i"]
        digitMap["5"] = ["j", "k", "l"]
        digitMap["6"] = ["m", "n", "o"]
        digitMap["7"] = ["p", "q", "r", "s"]
        digitMap["8"] = ["t", "u", "v"]
        digitMap["9"] = ["w", "x", "y", "z"]

        while digit:
            now = digit.pop()
            temp = []
            for c in digitMap[now]:
                for a in ans:
                    temp.append(c+a)
            ans = temp

        return ans
    

    def letterCombinations(self, digit) -> list[str]:

        if not digit:
            return []
        digitMap = defaultdict(list)

        digitMap["2"] = ["a", "b", "c"]
        digitMap["3"] = ["d", "e", "f"]
        digitMap["4"] = ["g", "h", "i"]
        digitMap["5"] = ["j", "k", "l"]
        digitMap["6"] = ["m", "n", "o"]
        digitMap["7"] = ["p", "q", "r", "s"]
        digitMap["8"] = ["t", "u", "v"]
        digitMap["9"] = ["w", "x", "y", "z"]

        ans = []
        N = len(digit)
        def backtrack(idx, curr):
            if idx == N:
                ans.append(curr)
                return
            
            for c in digitMap[digit[idx]]:
                backtrack(idx+1, curr + c)
                
        backtrack(0, "")
        return ans



    
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"))