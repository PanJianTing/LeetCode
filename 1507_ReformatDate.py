class Solution:
    def reformatDate(self, date: str) -> str:
        
        day, month, year = date.split(" ")
        monthDic = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12"}

        day = f"{int(day[:-2]):02d}"
        month = monthDic[month]


        return "-".join([year, month, day])



    def reformatDate_my(self, date: str) -> str:
        
        dateStrs = date.split(" ")
        monthDic = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12"}

        day = dateStrs[0].replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
        month = monthDic[dateStrs[1]]
        year = dateStrs[2]

        if len(day) == 1:
            day = "0" + day

        return year + "-" + month + "-" + day