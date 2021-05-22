class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:

        monthDic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        if M == 2:
            if Y % 100 == 0:
                if Y % 400 == 0:
                    return monthDic[2] + 1
            elif Y % 4 == 0:
                return monthDic[2] + 1
            else:
                return monthDic[2]

        return monthDic[M]


    def numberOfDays_my(self, Y: int, M: int) -> int:

        bigM = [1,3,5,7,8,10,12]
        smallM = [4,6,9,11]

        if M == 2:
            if Y % 400 == 0:
                return 29
            elif Y % 100 == 0:
                return 28
            elif Y % 4 == 0:
                return 29
            else:
                return 28
        else:
            if M in bigM:
                return 31
            elif M in smallM:
                return 30
