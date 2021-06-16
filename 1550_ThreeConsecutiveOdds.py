class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:

        count = 0

        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                if count == 2:
                    return True
                count += 1

        return False