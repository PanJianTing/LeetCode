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
    
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        res = 0
        
        for w in words:
            is_allow = True

            for c in w:
                is_char_allow = False

                for a in allowed:
                    if c == a:
                        is_char_allow = True
                        break
                if is_char_allow == False:
                    is_allow = False
                    break
            
            if is_allow:
                res += 1
        return res
    

    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        res = 0
        allow_list = [False] * 26

        for a in allowed:
            allow_list[ord(a) - ord('a')] = True

        for w in words:
            is_allow = True

            for c in w:
                if allow_list[ord(c) - ord('a')] == False:
                    is_allow = False
                    break
            if is_allow:
                res += 1
        return res
    

    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        res = 0
        allow_set = set()

        for a in allowed:
            allow_set.add(a)

        for w in words:
            is_allow = True

            for c in w:
                if c not in allow_set:
                    is_allow = False
                    break
            if is_allow:
                res += 1
        return res

    

print(Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(Solution().countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))