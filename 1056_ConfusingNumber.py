class Solution:
    # 若數字有非0,1,9,8,6的話，則直接False，若都是0,1,9,8,6，才用下述判斷
    # 計算倒過來後，是否跟原本的數相同，若相同則不是confusing，不同則是
    def confusingNumber(self, n: int) -> bool:

        checkTotal = 0
        # i = 0
        number = n

        while n > 0:
            checkNum = n % 10
            if checkNum == 0 or checkNum == 1 or checkNum == 8:
                checkTotal = checkTotal * 10 + checkNum
            elif checkNum == 6:
                checkTotal = checkTotal * 10 + 9
            elif checkNum == 9:
                checkTotal = checkTotal * 10 + 6
            else:
                return False
            n = n // 10
            # i = 1
        return not (checkTotal == number)


# print(Solution.confusingNumber(Solution(), 6))
# print(Solution.confusingNumber(Solution(), 11))
print(Solution.confusingNumber(Solution(), 916))