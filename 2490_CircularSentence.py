class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = sentence.split()
        sentence_list.append(sentence_list[0])
        N = len(sentence_list)

        for i in range(1, N):
            pre_char = sentence_list[i-1][-1]
            cur_char = sentence_list[i][0]

            if pre_char != cur_char:
                return False
        
        return True
    

    def isCircularSentence(self, sentence: str) -> bool:
        sen_list = sentence.split()
        N = len(sen_list)
        pre = sen_list[-1][-1]

        for i in range(N):
            cur = sen_list[i][0]

            if pre != cur:
                return False
            pre = sen_list[i][-1]
        return True
    

    def isCircularSentence(self, sentence: str) -> bool:
        N = len(sentence)

        for i in range(N):
            if sentence[i] == ' ' and sentence[i-1] != sentence[i+1]:
                return False
            
        return sentence[0] == sentence[-1]