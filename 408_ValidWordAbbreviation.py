class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        return self.valid_word_abbreviation(word, 0, abbr, 0)
        
    def iterative(self, word: str, abbr: str) -> bool:
        abbr_index = 0
        word_index = 0
        
        while abbr_index < len(abbr) and word_index < len(word):
            if word[word_index] == abbr[abbr_index]:
                word_index += 1
                abbr_index += 1
                continue
                
            elif abbr[abbr_index] == '0':
                return False
            elif abbr[abbr_index].isdigit():
                count = 0
                while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                    count = (count * 10) + int(abbr[abbr_index])
                    abbr_index += 1

                word_index += count
            
            else:
                return False
        
        return abbr_index == len(abbr) and word_index == len(word)
    
    def valid_word_abbreviation(self, word: str, word_index: int, abbr: str, abbr_index: int) -> bool:
        if word_index >= len(word) or abbr_index >= len(abbr):
            return word_index == len(word) and abbr_index == len(abbr)
        
        if word[word_index] == abbr[abbr_index]:
            return self.valid_word_abbreviation(word, word_index + 1, abbr, abbr_index + 1)
        
        if abbr[abbr_index] == '0':
            return False

        if abbr[abbr_index].isdigit():
            count = 0
            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                count = (count * 10) + int(abbr[abbr_index])
                abbr_index += 1
            
            return self.valid_word_abbreviation(word, word_index + count, abbr, abbr_index)
        
        return False




class Solution:
	def validWordAbbreviation(self, word: str, abbr: str) -> bool:
		checkIndex = 0
		num = 0

		for c in abbr:
			if c.isdigit():
				if num == 0 and c == "0":
					return False
				else:
					num = num * 10 + int(c)
			else:
				checkIndex += num
				num = 0

				if len(word) > checkIndex:
					if word[checkIndex] != c:
						return False
					else:
						checkIndex += 1
				else:
					return False
		return len(word) == checkIndex + num


	def validWordAbbreviation(self, word: str, abbr: str) -> bool:
		splitArr = []

		temp = ""

		for c in abbr:
			if c.isdigit():
				temp += c
			else:
				if len(temp) > 0:
					if temp[0] == '0':
						return False
					splitArr.append(temp)

				splitArr.append(c)
				temp = ""

		if len(temp) > 0:
			if temp[0] == '0':
				return False
			splitArr.append(temp)

		print(splitArr)
		checkIndex = 0

		for condition in splitArr:
			if condition.isdigit():
				checkIndex += int(condition)
			else:
				print(checkIndex, condition, word[checkIndex])
				if len(word) > checkIndex:
					if word[checkIndex] == condition:
						checkIndex += 1
					else:
						return False
				else:
					return False

		return len(word) == checkIndex