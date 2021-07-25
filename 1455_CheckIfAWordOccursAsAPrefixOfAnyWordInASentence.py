class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        sentenceList = sentence.split(" ")
        swLen = len(searchWord)

        for i in range(0, len(sentenceList)):
            word = sentenceList[i][:swLen]
            if len(sentenceList[i]) >= swLen and searchWord == word:
                return i + 1

        return -1