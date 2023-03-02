class Solution:
	def validWordSquare(self, words: list[str]) -> bool:
		for j in range(len(words)):
			for i in range(len(words[j])):

				if i < len(words) and j < len(words[i]):
					if words[j][i] != words[i][j]:
						return False
				else:
					return False
		return True
    
class Solution:
    def validWordSquare(self, words: list[str]) -> bool:

        afterWords = []

        for i in range(0, len(words)):
            str = ""
            for j in range(0, len(words)):

                if i < len(words[j]):
                    str += words[j][i]
            
            afterWords.append(str)

        for i in range(0, len(words)):
            if words[i] != afterWords[i]:
                return False
        return True
    
    def validWordSquare(self, words: list[str]) -> bool:

        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
                
        return True