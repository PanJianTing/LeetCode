class Solution:
    def numberToWords(self, num: int) -> str:
        tag = ['', 'Thousand', 'Million', 'Billion']
        tag_10 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        tag_0 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        idx = 0
        res = []
        
        if num == 0:
            return tag_0[0]

        while num > 0:
            cur = num % 1000

            if idx > 0 and cur > 0:
                res.append(tag[idx])

            million = cur // 100
            ten = cur % 100
            if ten > 0:
                if ten > 19:
                    digit = ten % 10
                    ten = ten // 10
                    if digit > 0:
                        res.append(tag_0[digit])
                    res.append(tag_10[ten])
                else:
                    res.append(tag_0[ten])
            
            if million > 0:
                res.append("Hundred")
                res.append(tag_0[million])

            num //= 1000
            idx += 1

        res.reverse()
        return ' '.join(res)
    

    def numberToWords(self, num: int) -> str:
        digit = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        below_100 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def helper(num):

            if num < 20:
                s = digit[num]
            elif 20 <= num < 100:
                s = below_100[num // 10] + " " + helper(num % 10)
            elif 100 <= num < 1000:
                s = helper(num // 100) + " Hundred " + helper(num % 100)
            elif 1000 <= num < 1000000:
                s = helper(num // 1000) + " Thousand " + helper(num % 1000)
            elif 1000000 <= num < 1000000000:
                s = helper(num // 1000000) + " Million " + helper(num % 1000000)
            elif 1000000000 <= num:
                s = helper(num // 1000000000) + " Billion " + helper(num % 1000000000)
            return s.strip()
        
        if num == 0:
            return "Zero"
        return helper(num)
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        digit = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        below_100 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        tag = ['', 'Thousand', 'Million', 'Billion']

        res = ""
        idx = 0

        while num > 0:
            if num % 1000 > 0:
                group = ""

                part = num % 1000

                if (part // 100) > 0:
                    group += digit[part // 100] + " Hundred "
                    part %= 100
                
                if part > 19:
                    group += below_100[part // 10] + " "
                    part %= 10
                
                if part > 0:
                    group += digit[part] + " "

                group += tag[idx] + " "
                res = group + res
            
            idx += 1
            num //= 1000
        return res.strip()
    

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        value_map = { 1000000000 : 'Billion', 1000000 : 'Million', 1000 : 'Thousand', 100 : 'Hundred',
                     90 : 'Ninety',  80 : 'Eighty', 70 : 'Seventy', 60 : 'Sixty', 
                     50 : 'Fifty', 40 : 'Forty', 30 : 'Thirty', 20 : 'Twenty',
                     19 : 'Nineteen', 18 : 'Eighteen', 17 : 'Seventeen', 16 : 'Sixteen', 15 : 'Fifteen', 14 : 'Fourteen', 13 : 'Thirteen', 12 : 'Twelve', 11 : 'Eleven',
                     10 : 'Ten', 9 : 'Nine', 8 : 'Eight', 7 : 'Seven', 6 : 'Six', 5 : 'Five', 4 : 'Four', 3 : 'Three', 2 : 'Two', 1 : 'One'}
        
        def helper(cur):

            for v, s in value_map.items():
                
                if cur >= v:

                    prefix = (helper(cur // v) + " ") if cur >= 100 else  "" 

                    unit = s

                    suffix = "" if cur % v  == 0 else " " + helper(cur % v)

                    return prefix + unit + suffix
                
            return ""

        return helper(num)

    
print(Solution().numberToWords(0))
print(Solution().numberToWords(1000000))
print(Solution().numberToWords(20))
print(Solution().numberToWords(123))
print(Solution().numberToWords(100))
print(Solution().numberToWords(101))
print(Solution().numberToWords(999))
print(Solution().numberToWords(1000))
print(Solution().numberToWords(12345))
print(Solution().numberToWords(1234567))