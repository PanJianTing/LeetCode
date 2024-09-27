from collections import defaultdict

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        N = len(words)
        prefix_map = defaultdict(int)
        res = [0] * N

        for i in range(N):
            cur_word = words[i]
            for j in range(len(cur_word)):
                cur_prefix = cur_word[:j+1]
                prefix_map[cur_prefix] += 1


        for i in range(N):
            cur_word = words[i]
            for j in range(len(cur_word)):
                cur_prefix = cur_word[:j+1]
                res[i] += prefix_map[cur_prefix]
        
        return res

    def sumPrefixScores(self, words: list[str]) -> list[int]:
        N = len(words)
        prefix_cnt_map = defaultdict(int)
        all_prefix_map = defaultdict(set)
        res = [0] * N

        for i in range(N):
            cur_word = words[i]
            for j in range(len(cur_word)):
                cur_prefix = cur_word[:j+1]
                all_prefix_map[i].add(cur_prefix)
                prefix_cnt_map[cur_prefix] += 1


        for i in range(N):
            for cur_prefix in all_prefix_map[i] :
                res[i] += prefix_cnt_map[cur_prefix]
        
        return res
    

print(Solution().sumPrefixScores(["abc","ab","bc","b"]))


        
