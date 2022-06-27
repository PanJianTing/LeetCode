import datetime
from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_name = datetime.date(year, month, day)
        return day_name.strftime("%A")

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        sumOfDay = day
        dayOfMonth = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        weekName = {
            0 : "Thursday", 
            1 : "Friday",
            2 : "Saturday", 
            3 : "Sunday", 
            4 : "Monday", 
            5:"Tuesday", 
            6:"Wednesday"}

        for y in range(1971, year):
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                sumOfDay += 366
            else:
                sumOfDay += 365

        for m in range(1, month):
            if m == 2:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    sumOfDay += 29
                    continue
            sumOfDay += dayOfMonth[m]

        return weekName[(sumOfDay)%7]

# Solution().dayOfTheWeek(2, 1, 1971)
# Solution().dayOfTheWeek(31, 8, 2019)
# Solution().dayOfTheWeek(18, 7, 1999)
# Solution().dayOfTheWeek(15, 8, 1993)
Solution().dayOfTheWeek(31, 8, 2100)