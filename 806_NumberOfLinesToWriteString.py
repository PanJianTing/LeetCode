class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:

        lines = 0
        lastPixel = 0

        charDic = {}

        for i in range(0, 26):
            char = chr(97 + i)
            charDic[char] = widths[i]

        print(charDic)

        for char in s:
            lastPixel += charDic[char]
            if lastPixel == 100:
                lines += 1
                lastPixel = 0
            elif lastPixel > 100:
                lines += 1
                lastPixel = charDic[char]


        if lastPixel > 0:
            lines += 1
        else:
            lastPixel = 100

        return [lines, lastPixel]

    def numberOfLines(self, widths: list[int], s: str) -> list[int]:

        lines = 0
        lastPixel = 0

        for char in s:
            w = widths[ord(char) - 97]
            lastPixel += w
            if lastPixel > 100:
                lines += 1
                lastPixel = w


        if lastPixel > 0:
            lines += 1
        else:
            lastPixel = 100

        return [lines, lastPixel]

    def numberOfLines(self, widths: list[int], s: str) -> list[int]:

        lines = 1
        lastPixel = 0

        for char in s:
            w = widths[ord(char) - 97]
            lastPixel += w
            if lastPixel > 100:
                lines += 1
                lastPixel = w

        return [lines, lastPixel]
        

print(Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print(Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))