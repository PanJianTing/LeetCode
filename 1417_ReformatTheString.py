class Solution:
    def reformat(self, s: str) -> str:
        
        nums = []
        letter = []

        for c in s:
            if c.isalpha():
                letter.append(c)
            elif c.isdigit():
                nums.append(c)

        resultStr = ""

        if abs(len(letter) - len(nums)) > 1:
            return resultStr

        first, later = nums, letter

        if len(later) > len(first):
            first, later = later, first

        count = len(later)
        for i in range(count):
            resultStr += first[i] + later[i]

        if len(first) > len(later):
            resultStr += first[-1]

        return resultStr

    def reformat_my(self, s: str) -> str:
        
        nums = []
        letter = []

        for c in s:
            if c.isalpha():
                letter.append(c)
            elif c.isdigit():
                nums.append(c)


        resultStr = ""

        if abs(len(letter) - len(nums)) < 2:
            if len(letter) > len(nums):
                while len(letter) or len(nums):
                    if len(letter):
                        resultStr += letter.pop(0)
                    if len(nums):
                        resultStr += nums.pop(0)
            else:
                while len(letter) or len(nums):
                    if len(nums):
                        resultStr += nums.pop(0)
                    if len(letter):
                        resultStr += letter.pop(0)
        return resultStr