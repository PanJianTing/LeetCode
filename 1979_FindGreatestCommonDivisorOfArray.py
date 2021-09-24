class Solution:

    # 輾轉相除法
    def findGCD(self, nums: list[int]) -> int:
        x, y = min(nums), max(nums)

        x = 1071
        y = 462

        while y :
            x, y = y, x % y

        return x

    def findGCD(self, nums: list[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        ans = minNum

        for i in range(minNum, 1, -1):
            if maxNum % i == 0 and minNum % i == 0:
                return i
        
        return 1



    def findGCD_my(self, nums: list[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        ans = 1

        for i in range(1, minNum + 1):
            if maxNum % i == 0 and minNum % i == 0:
                if i > ans:
                    ans = i
        
        return ans


# Solution.findGCD(Solution(), [2,5,6,9,10])

Solution.test(Solution(), 1071, 462)