class Solution:
    def countElements(self, arr: list[int]) -> int:
        res = 0
        s = set(arr)

        for count in arr:
            if count + 1 in s:
                res += 1

        return res


    def countElements_my(self, arr: list[int]) -> int:
        res = 0
        for count in arr:
            if count + 1 in arr:
                res += 1

        return res