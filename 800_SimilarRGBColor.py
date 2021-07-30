class Solution:
    def findSimilar(self, color: str) -> str:

        digit, mod = divmod(int("0x" + color, 16), 17)
        if mod > 8:
            digit += 1

        #{:x} -> 代表16進位，02代表兩位，不齊補0
        return "{:02x}".format(digit*17)

    def similarRGB(self, color: str) -> str:
        return "#" + self.findSimilar(self, color[1:3]) + self.findSimilar(self, color[3:5]) + self.findSimilar(self, color[5:])



    def similarRGB_my2(self, color: str) -> str:

        similarList = ["0x00", "0x11", "0x22", "0x33", "0x44", "0x55", "0x66", "0x77", "0x88", "0x99", "0xaa", "0xbb", "0xcc", "0xdd", "0xee", "0xff"]

        colorList = []

        result = ""

        for i in range(1, len(color), 2):
            colorList.append(color[i:i+2])

        for c in colorList:
            if c[0] != c[1]:
                # 因為相差11(16)->17(10)，故要除以17
                digit, mod = divmod(int("0x" + c, 16), 17)
                if mod > 8:
                    digit += 1
                result += similarList[digit][-2:]
            else:
                result += c
        return "#" + result


    def similarRGB_my(self, color: str) -> str:

        similarList = ["0x00", "0x11", "0x22", "0x33", "0x44", "0x55", "0x66", "0x77", "0x88", "0x99", "0xaa", "0xbb", "0xcc", "0xdd", "0xee", "0xff"]

        colorList = []

        result = ""

        for i in range(1, len(color), 2):
            colorList.append(color[i:i+2])

        for c in colorList:
            if c[0] != c[1]:
                digit = int("0x" + c, 16)
                small = 99999
                similarDigit = ""
                for similiar in similarList:
                    if abs(digit - int(similiar,16)) < small:
                        small = abs(digit - int(similiar,16))
                        similarDigit = similiar[-2:]
                result += similarDigit

            else:
                result += c
        return "#" + result


Solution.similarRGB(Solution, "#09f166")