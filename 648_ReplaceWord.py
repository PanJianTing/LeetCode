class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        sen_list = sentence.split(" ")
        N = len(dictionary)
        M = len(sen_list)

        for i in range(N):
            word = dictionary[i]
            w_len = len(word)
            for j in range(M):
                sen = sen_list[j]
                if len(sen) > w_len and sen[:w_len] == word:
                    sen_list[j] = word

        return ' '.join(sen_list)
    
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        d_map = {w: len(w) for w in dictionary}
        min_l = float("inf")
        max_l = float("-inf")
        sen_list = sentence.split()
        
        for w in d_map.keys():
            min_l = min(min_l, d_map[w])    
            max_l = max(max_l, d_map[w])

        for i, sen in enumerate(sen_list):

            for j in range(min_l, max_l+1):
                if sen[:j] in d_map:
                    sen_list[i] = sen[:j]
                    break
        return " ".join(sen_list)
    
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dict_set = set(dictionary)
        sentence = sentence.split()
        min_l = min([len(w) for w in dict_set])
        max_l = max([len(w) for w in dict_set])
        
        N = len(sentence)

        def getShortest(w):    
            for i in range(min_l, max_l+1):
                if w[:i] in dict_set:
                    return w[:i]
            return w
        
        for i in range(N):
            sentence[i] = getShortest(sentence[i])
        
        return " ".join(sentence)






print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(Solution().replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))


        
