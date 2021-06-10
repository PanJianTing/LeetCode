class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        allSum = sum(nums)
        setSum = sum(set(nums))
        allRangeSum = sum(range(1, len(nums) + 1))

        return [allSum - setSum, allRangeSum - setSum]


    def findErrorNums_my(self, nums: list[int]) -> list[int]:
        count = len(nums)
        allSum = ((1+count) * count)//2

        nowDic = {}
        repeatCount = 0

        for n in nums:
            if n not in nowDic:
                allSum -= n
                nowDic[n] = 1
            else:
                repeatCount = n


        return [repeatCount, allSum]


Solution.findErrorNums(Solution(), [1,2,2,4])