class Solution:

    # 必須要大過相加過程中的最小數+1
    def minStartValue(self, nums: list[int]) -> int:
        min_sum = 0
        cur_sum = 0

        for num in nums:
            cur_sum += num
            min_sum = min(min_sum, cur_sum)

        if min_sum > 0:
            return 1
        
        return 1 - min_sum

    def minStartValue_my(self, nums: list[int]) -> int:
        
        value = 1
        while True:
            sum = value
            isOK = True
            for num in nums:
                sum += num
                if sum < 1:
                    isOK = False
                    break

            if isOK:
                break
            
            value += 1

        return value


Solution.minStartValue(Solution(), [-3,2,-3,4,2])