class Solution:
    def dayOfYear(self, date: str) -> int:

        dataList = date.split("-")

        year = int(dataList[0])
        month = int(dataList[1])
        day = int(dataList[2])

        
        monthDic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        if year % 100 == 0:
            if year % 400 == 0:
                monthDic[2] += 1
        elif year % 4 == 0:
            monthDic[2] += 1
        
        for i in range(1, month):
            day += monthDic[i]
            

        return day
