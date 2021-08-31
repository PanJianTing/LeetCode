import bisect

class Solution:
    # 每個元素遍歷
    def findTheDistanceValue_slow(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for num in arr1:
            if all([abs(x - num) > d for x in arr2]) == True:
                ans += 1

        return ans
            
    # 二分法。
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2 = sorted(arr2)
        ans = 0
        for num1 in arr1:
            index = bisect.bisect_left(arr2, num1)
            arr3 = arr2[0:index]
            arr4 = arr2[index:]
            
            if len(arr3) == 0:
                if abs(arr4[0] - num1) > d:
                    ans += 1
            elif len(arr4) == 0:
                if abs(arr3[-1] - num1) > d:
                    ans += 1
            else:
                if abs(arr3[-1] - num1) > d and abs(arr4[0] - num1) > d:
                    ans += 1
        return ans



# Solution.findTheDistanceValue(Solution(), [1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3)
Solution.findTheDistanceValue(Solution(), [2, 1, 100, 3], [-5, -2, 10, -3, 7], 6)