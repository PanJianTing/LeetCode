class Solution:


    def largestOddNumber(self, num: str) -> str:

        for i in range(len(num)-1, -1 ,-1):
            if num[i] in {"1", "3", "5", "7", "9"}:
                return num[:i+1]
        return ""



    def largestOddNumber_my(self, num: str) -> str:
        
        num = int(num)
        largest = 0

        while num > 0:
            if num % 2 == 1:
                return str(num)
            else:
                num = num // 10

        if largest == 0:
            return ""
        return str(largest)