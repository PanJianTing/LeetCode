class Solution:
    def dietPlanPerformance(self, calories: list[int], k: int, lower: int, upper: int) -> int:
        result = 0
        total = 0
        for i in range(0, len(calories)):
            if i - k >= 0:
                total -= calories[i-k]
            total += calories[i]
            if i+1 >= k:
                result += (total > upper) - (total < lower)
        return result


    #一直加，加超出K時，再往前減掉
    def dietPlanPerformance_2(self, calories: list[int], k: int, lower: int, upper: int) -> int:
        result = 0
        cals = sum(calories[0: k-1])
        for i in range(k-1, len(calories)):
            temp = calories[i-k] * (i-k >= 0)
            cals += calories[i] - temp
            result += (cals > upper) - (cals < lower)
        return result


    def dietPlanPerformance_1(self, calories: list[int], k: int, lower: int, upper: int) -> int:

        result = 0
        sub = calories[0:k]
        total = sum(sub)
        
        if total > upper:
            result += 1
        elif total < lower:
            result -= 1

        for i in range(k, len(calories)):
            total = total - sub[0] + calories[i]
            if total > upper:
                result += 1
            elif total < lower:
                result -= 1
            sub.pop(0)
            sub.append(calories[i])

        return result




    def dietPlanPerformance_timeout(self, calories: list[int], k: int, lower: int, upper: int) -> int:

        result = 0
        count = len(calories)

        for i in range(0, count):
            if i + k < count + 1:
                total = sum(calories[i:i+k])
                if total < lower:
                    result -= 1
                elif total > upper:
                    result += 1

        return result


# print(Solution.dietPlanPerformance(Solution(), [1,2,3,4,5], 1, 3, 3))
print(Solution.dietPlanPerformance(Solution(), [3,2], 2, 0, 1))