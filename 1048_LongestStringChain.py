from functools import cache
from collections import defaultdict

class Solution:
    def longestStrChain(self, words):
        word_length = len(words)
        words = sorted(words, key= lambda x:len(x))

        def check(a, b):
            M = len(a)
            N = len(b)

            if M > N:
                return check(b, a)

            if N - M > 1 or M == N:
                return False
            pa = 0
            pb = 0

            while pa < M and pb < N:
                if a[pa] == b[pb]:
                    pa += 1
                pb += 1
            return pa == M
        
        dp = [1] * (word_length+1)

        for i in range(1, word_length):
            temp = dp[i]
            for j in range(i-1, -1, -1):
                if check(words[i], words[j]):
                    temp = max(temp, 1 + dp[j])
                
            dp[i] = temp
        
        return max(dp)
    
    def longestStrChain(self, words):

        N = len(words)

        words = set(words)

        @cache
        def dfs(curwords): 

            max_length = 1

            for i in range(len(curwords)):
                temp = curwords[:i] + curwords[i+1:]
                if temp in words:
                    max_length = max(max_length, 1 + dfs(temp))

            return max_length

        ans = 0
        for w in words:
            ans = max(ans, dfs(w))
        
        return ans
    
    def longestStrChain(self, words):

        words = sorted(words, key=lambda x: len(x))
        longest = 1
        word_length_dic = defaultdict(int)

        for w in words:
            cur_length = 1
            for i in range(0, len(w)):
                check_word = w[:i] + w[i+1:]
                cur_length = max(cur_length, 1 + word_length_dic[check_word])
            
            word_length_dic[w] = cur_length
            longest = max(longest, cur_length)

        return longest



#4
print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))

#5
print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))

#1
print(Solution().longestStrChain(["abcd","dbqca"]))

#7
print(Solution().longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))

#2
print(Solution().longestStrChain(["a","b","ab","bac"]))

#4
print(Solution().longestStrChain(["a","ab","ac","bd","abc","abd","abdd"]))

