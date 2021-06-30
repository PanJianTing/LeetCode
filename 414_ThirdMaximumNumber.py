class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        numberSet = set(nums)

        if len(numberSet) < 3:
            return max(numberSet)

        firstNum = max(numberSet)
        numberSet.remove(firstNum)
        sencondNum = max(numberSet)
        numberSet.remove(sencondNum)
        
        return max(numberSet)

    def thirdMax_my(self, nums: list[int]) -> int:

        distinctList = []

        for num in nums:
            if num not in distinctList:
                distinctList.append(num)
        
        if len(distinctList) < 3:
            return max(distinctList)

        
        distinctList = sorted(distinctList, reverse=True)

        return distinctList[2]

Solution.thirdMax(Solution(), [1,2,3,3,2,1])