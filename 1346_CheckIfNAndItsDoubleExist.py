import collections
from typing import Collection


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        # 先查看0的數量，有兩個以上，則必為True
        s = collections.Counter(arr)
        if s[0] > 1: return True

        for num in arr:
            if num * 2 in arr and num != 0:
                return True
        return False

    def checkIfExist_my(self, arr: list[int]) -> bool:

        for i in range(len(arr)):
            doubleNum = 2 * arr[i]
            if doubleNum in arr:
                for j in range(len(arr)):
                    if i != j and doubleNum == arr[j]:
                        return True
        return False


# Solution.checkIfExist(Solution(), [0, 0])
Solution.checkIfExist(Solution(), [-2,0,10,-19,4,6,-8])