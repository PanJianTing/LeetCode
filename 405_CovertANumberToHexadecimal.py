class Solution:
    def toHex(self, num: int) -> str:

        if num >= 0:
            return hex(num)[2:]
        else:
            print(2**32)
            return hex(2**32 + num)[2:]

    def toHex(self, num: int) -> str:

        result = ""

        hexMap = {
            0:"0",
            1:"1",
            2:"2",
            3:"3",
            4:"4",
            5:"5",
            6:"6",
            7:"7",
            8:"8",
            9:"9", 
            10:"a", 
            11:"b", 
            12:"c", 
            13:"d", 
            14:"e", 
            15:"f"}

        if num == 0:
            return "0"

        if num < 0:
            num = 4294967296 - num * -1

        while num > 0:
            digit = num % 16
            num //= 16

            result += hexMap[digit]

        return result[::-1]

print(Solution.toHex(Solution(), -1))