import datetime

# 換算成天數，在相減
class Solution:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    presum = [0] * 13

    def isLeap(self, y: int) -> bool:
        return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    
    def toDays(self, date: str) -> int:
        y, m, d = map(int, date.split("-"))
        # 算從1971開始，有幾年是閏年，是閏年則須加1
        n = sum(self.isLeap(x) for x in range(1971, y))
        # 算從1971年起，過了幾天，再加上閏年天數。
        res = 365 * (y - 1971) + n
        # 算y年起過了幾月，如果y年是閏年，月份大於2則須加1，再加上天數。
        res += self.presum[m - 1] + (m > 2 and self.isLeap(y)) + d
        return res
    

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        for i in range(12):
            self.presum[i + 1] = self.presum[i] + self.days[i]
        return abs(self.toDays(date1) - self.toDays(date2))


class Solution_my:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        dateArray1 = date1.split("-")
        dateArray2 = date2.split("-")

        datetime1 = datetime.datetime(int(dateArray1[0]), int(dateArray1[1]), int(dateArray1[2]))
        datetime2 = datetime.datetime(int(dateArray2[0]), int(dateArray2[1]), int(dateArray2[2]))

        return abs((datetime2 - datetime1).days)

Solution.daysBetweenDates(Solution(), "2020-01-15", "2019-12-31")