from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        N = len(s)
        word_set = set(wordDict)
        res = []
        
        def dp(idx, cur):
            if idx == N:
                res.append(" ".join(cur))

            for i in range(idx, N):
                cur_word = s[idx:i+1]
                if cur_word in word_set:
                    cur.append(cur_word)
                    dp(i+1, cur)
                    cur.pop()
        dp(0, [])
        return res
    


    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        N = len(s)
        dp = defaultdict(list)
        wordSet = set(wordDict)

        for st in range(N, -1, -1):
            valid = []
            for end in range(st, N):
                cur_word = s[st:end+1]
                print(cur_word)
                if cur_word in wordSet:
                    if end == N-1:
                        valid.append(cur_word)
                    else:
                        after_res = dp[end+1]
                        for sentance in after_res:
                            valid.append(cur_word + " " + sentance)
            dp[st] = valid
        return dp[0]
        


            
    
print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
