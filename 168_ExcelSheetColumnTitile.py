class Solution:

    def convertToTitle(self, columnNumber: int) -> str:

        title = ""

        while columnNumber > 0:
            letter = chr(ord('A') + (columnNumber-1)%26)
            title = letter + title
            columnNumber = (columnNumber -1)//26

        return title

    def convertToTitle_my(self, columnNumber: int) -> str:

        letterArray = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
        title = ""

        while columnNumber > 0:
            letterIndex = columnNumber % 26
            title = letterArray[letterIndex] + title
            columnNumber //= 26

            if letterIndex == 0:
                columnNumber -= 1

        return title


print(Solution().convertToTitle(26))
print(Solution().convertToTitle(27))
print(Solution().convertToTitle(52))
print(Solution().convertToTitle(676))
print(Solution().convertToTitle(701))
print(Solution().convertToTitle(2147483647))
