class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:

        if ch in word:
            index = word.index(ch)
            return word[:index + 1][::-1] + word[index + 1:]
        return word



    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        
        if index == -1:
            return word
        else:
            return word[:index+1][::-1] + word[index+1:]


    def reversePrefix_my(self, word: str, ch: str) -> str:
        
        if ch not in word:
            return word

        reverseList = []

        for i in range(len(word)):
            c = word[i]
            reverseList.append(c)
            if c == ch:
                word = word[i+1:]
                break
        
        return "".join(reverseList[::-1]) + word


