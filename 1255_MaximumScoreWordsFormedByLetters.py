from collections import defaultdict

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        N = len(words)
        all_letter_cnt = defaultdict(int)
        base = ord('a')

        for l in letters:
            all_letter_cnt[l] += 1
        
        def backtrack(cur, letter_cnt, cur_score):
            if cur == N:
                return cur_score
            
            skip = backtrack(cur+1, letter_cnt, cur_score)

            temp = 0
            isvalid = True
            take = 0
            cur_letter_map = defaultdict(int)
            for i in range(len(words[cur])):
                cur_letter_map[words[cur][i]] += 1
            
            for letter in cur_letter_map.keys():
                if cur_letter_map[letter] > letter_cnt[letter]:
                    isvalid = False
                    break
            
            if isvalid:
                for i in range(len(words[cur])):
                    letter_cnt[words[cur][i]] -= 1
                    temp += score[ord(words[cur][i]) - base]
                take = backtrack(cur+1, letter_cnt, cur_score + temp)

                for letter in cur_letter_map.keys():
                    letter_cnt[letter] += cur_letter_map[letter]
            
            return max(skip, take)
        return backtrack(0, all_letter_cnt, 0)
    
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        N = len(words)
        all_letter_cnt = defaultdict(int)
        base = ord('a')
        res = 0

        for l in letters:
            all_letter_cnt[l] += 1

        def calScore(words_map):
            set_score = 0
            for l in words_map.keys():
                if words_map[l] <= all_letter_cnt[l]:
                    set_score += words_map[l] * score[(ord(l) - base)]
                else:
                    return 0
            return set_score

        for mask in range((1 << N)):
            cur = 0
            cur_word_cnt = defaultdict(int)
            while mask > 0:
                if (mask & 1):
                    cur_word = words[cur]
                    for c in cur_word:
                        cur_word_cnt[c] += 1
                cur += 1
                mask >>= 1
            res = max(res, calScore(cur_word_cnt))
        return res
    
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        N = len(words)
        all_letter_cnt = defaultdict(int)
        base = ord('a')
        res = 0

        for l in letters:
            all_letter_cnt[l] += 1

        def calScore(words_map):
            set_score = 0
            for l in words_map.keys():
                if words_map[l] <= all_letter_cnt[l]:
                    set_score += words_map[l] * score[(ord(l) - base)]
                else:
                    return 0
            return set_score

        for mask in range((1 << N)):
            cur_word_cnt = defaultdict(int)
            for i in range(N):
                if (mask & (1 << i)):
                    cur_word = words[i]
                    for c in cur_word:
                        cur_word_cnt[c] += 1
            res = max(res, calScore(cur_word_cnt))

        return res
    

    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        N = len(words)
        all_letter_map = defaultdict(int)
        
        for l in letters:
            all_letter_map[l] += 1
        
        def isValid(letter_map):
            for l in letter_map.keys():
                if letter_map[l] > all_letter_map[l]:
                    return False
            return True
        
        def calScore(word):
            res = 0
            for l in word:
                res += score[ord(l) - 97]
            return res 


        def backtrack(cur, cur_map, cur_score):
            if cur == N:
                return cur_score
            
            skip = backtrack(cur+1, cur_map, cur_score)
            take = 0
            
            for l in words[cur]:
                cur_map[l] += 1
            
            if (isValid(cur_map)):
                take = backtrack(cur+1, cur_map, cur_score + calScore(words[cur]))
            
            for l in words[cur]:
                cur_map[l] -= 1
            
            return max(skip, take)
        
        return backtrack(0, defaultdict(int), 0)






   
print(Solution().maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
print(Solution().maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
print(Solution().maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))
        