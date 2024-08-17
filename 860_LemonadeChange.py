class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bill_map = {5:0, 10: 0}

        for b in bills:
            if b == 5:
                bill_map[5] += 1
            elif b == 10:
                if bill_map[5] > 0:
                    bill_map[5] -= 1
                    bill_map[10] += 1
                else:
                    return False
            else:
                if bill_map[10] > 0 and bill_map[5] > 0:
                    bill_map[10] -= 1
                    bill_map[5] -= 1
                elif bill_map[5] >= 3:
                    bill_map[5] -= 3
                else:
                    return False
        return True
    
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0
        
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        return True
    
print(Solution().lemonadeChange([5,5,5,10,20]))
print(Solution().lemonadeChange([5,5,10,10,20]))

        