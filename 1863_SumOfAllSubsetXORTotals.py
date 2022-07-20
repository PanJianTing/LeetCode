class Solution:
    # https://home.gamer.com.tw/artwork.php?sn=5206551
    # def subsetXORSum(self, nums: list[int]) -> int:
        
    #     orSum = 0

    #     for num in nums:
    #         orSum |= num
        
    #     return pow(2, len(nums) -1) * orSum
        




    def subsetXORSumRec(self, nums: list[int], retSum: int, pos: int) -> int:
        print("sum : ", retSum, " pos : ", pos)
        if pos == len(nums):
            return retSum
        return self.subsetXORSumRec(nums, retSum ^ nums[pos], pos + 1) + self.subsetXORSumRec(nums, retSum, pos + 1)


    def subsetXORSum(self, nums: list[int]) -> int:
        return self.subsetXORSumRec(nums, 0, 0)


Solution.subsetXORSum(Solution(), [1,3])