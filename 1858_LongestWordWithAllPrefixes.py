class Solution:
    def longestWord(self, words: list[str]) -> str:
        check_set = set(words)
        words.sort()
        cur_len = 0
        res = ""

        for w in words:
            is_res = True
            for i in range(len(w)):
                if w[:i+1] not in check_set:
                    is_res = False
                    break
            if is_res:
                if len(w) > cur_len:
                    res = w
                    cur_len = len(w)
        return res
    
    
    def longestWord(self, words: list[str]) -> str:
        res = ''
        valid_set = set()
        words.sort()

        for w in words:
            if len(w) == 1 or w[:-1] in valid_set:
                valid_set.add(w)
                if len(w) > len(res):
                    res = w
        
        return res
    

print(Solution().longestWord(["k","ki","kir","kira","kiran"]))
print(Solution().longestWord(["a","banana","app","appl","ap","apply","apple"]))
print(Solution().longestWord(["abc","bc","ab","qwe"]))
