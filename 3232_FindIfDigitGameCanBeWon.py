class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        one_sum = 0
        two_sum = 0

        for n in nums:
            if n < 10:
                one_sum += n
            else:
                two_sum += n
        
        return (one_sum == two_sum) == False