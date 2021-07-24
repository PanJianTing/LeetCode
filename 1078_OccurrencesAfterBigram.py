class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:

        textList = text.split(" ")
        result = list()

        for i in range(0, len(textList) - 2):
            t1 = textList[i]
            t2 = textList[i+1]
            t3 = textList[i+2]

            if t1 == first and t2 == second:
                result.append(t3)

        return result