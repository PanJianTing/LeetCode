class Solution:
    def generateAbbreviations(self, word: str) -> list[str]:
        N = len(word)
        self.res = []

        def backtract(idx, cur_word, cur_cnt):

            if idx == N:
                if cur_cnt > 0:
                    cur_word += str(cur_cnt)
                self.res.append(cur_word)
                return
            
            backtract(idx+1, cur_word, cur_cnt+1)
            if cur_cnt > 0:
                backtract(idx+1, cur_word + str(cur_cnt) + word[idx], 0)
            else:
                backtract(idx+1, cur_word + word[idx], 0)
        backtract(0, "", 0)
        return self.res
    

print(Solution().generateAbbreviations("word"))
            

        