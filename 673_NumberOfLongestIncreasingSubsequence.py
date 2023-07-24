class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        N = len(nums)
        length = [1] * N
        count = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        maxl = max(length)
        res = 0

        for i in range(N):
            if length[i] == maxl:
                res += count[i]

        return res
    
    def calculateDP(self, i, nums, length, count):
        if length[i] != 0:
            return
        length[i] = 1
        count[i] = 1

        for j in range(i):
            if nums[j] < nums[i]:
                self.calculateDP(j, nums, length, count)
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = 0
                if length[j] + 1 == length[i]:
                    count[i] += count[j]


    def findNumberOfLIS(self, nums: list[int]) -> int:
        N = len(nums)
        length = [0] * N
        count = [0] * N
        maxLength = 0
        res = 0

        for i in range(N):
            self.calculateDP(i, nums, length, count)
            maxLength = max(maxLength, length[i])
        
        for i in range(N):
            if length[i] == maxLength:
                res += count[i]
        return res
            



