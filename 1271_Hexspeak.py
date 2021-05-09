class Solution:

    def toHexspeak(self, num: str) -> str:
        
        n = int(num)

        convertDic = {10: "A", 11:"B", 12: "C", 13:"D", 14: "E", 15:"F", 1: "I", 0:"O"}

        hexspeak = ""

        while n > 0:
            digit = n % 16
            if digit in convertDic:
                hexspeak = convertDic[digit] + hexspeak
            else:
                return "ERROR"
            n //= 16

        return hexspeak



    def toHexspeak_my(self, num: str) -> str:
        
        n = int(num)

        convertDic = {10: "A", 11:"B", 12: "C", 13:"D", 14: "E", 15:"F", 1: "I", 0:"O"}

        hexspeak = ""

        while n > 0:
            digit = n % 16
            if digit in convertDic:
                hexspeak += convertDic[digit]
            else:
                return "ERROR"
            n //= 16

        return hexspeak[::-1]