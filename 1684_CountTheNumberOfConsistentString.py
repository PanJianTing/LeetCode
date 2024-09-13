class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        word_set = []
        allowed = set(allowed)
        res = 0

        for w in words:
            word_set.append(set(w))
        
        for w in word_set:
            if len(w - allowed) == 0:
                res += 1
        return res
    

print(Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(Solution().countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))