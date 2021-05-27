class Solution:
    def sortSentence(self, s: str) -> str:
        sentenceList = s.split()
        sentenceList.sort(key=lambda w:w[-1])
        return " ".join(w[:-1] for w in sentenceList)

    def sortSentence_my(self, s: str) -> str:
        sentenceList = s.split(" ")

        sentenceMap = {}

        result = ""

        for sentence in sentenceList:
            index = int(sentence[-1])
            sentenceMap[index] = sentence[:-1]
        
        for i in range(1, len(sentenceMap.keys()) + 1):

            result += sentenceMap[i] + " "

        return result[:-1]



Solution.sortSentence(Solution(), "is2 sentence4 This1 a3")