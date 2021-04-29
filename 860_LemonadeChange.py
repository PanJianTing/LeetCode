class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
    
    def lemonadeChange_my(self, bills: list[int]) -> bool:
        nowBills = {
            5:0,
            10:0
        }
        
        for bill in bills:
            if bill == 5:
                nowBills[bill] += 1
            elif bill == 10:
                if nowBills[5] == 0:
                    return False
                else:
                    nowBills[5] -= 1
                    nowBills[10] += 1
            elif bill == 20:
                if nowBills[10] > 0:
                    if nowBills[5] == 0:
                        return False:
                    else:
                        nowBills[10] -= 1
                        nowBills[5] -= 1
                else:
                    if nowBills[5] < 3:
                        return False:
                    else:
                        nowBills[5] -= 3

        return True
                

print("Hello World!")