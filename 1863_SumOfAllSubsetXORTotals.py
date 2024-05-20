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
    

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        subset = []

        def generateSubset(idx, cur):
            if idx == N:
                if len(cur) > 0:
                    subset.append(cur)
                return
            temp = list(cur)
            generateSubset(idx+1, temp)
            temp2 = list(cur)
            temp2.append(nums[idx])
            generateSubset(idx+1, temp2)
            return
        generateSubset(0, [])
        for i in range(len(subset)):
            cnt = len(subset[i])
            temp = 0
            for j in range(cnt):
                temp ^= subset[i][j]
            res += temp
        return res
    

    def subsetXORSum(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        subset = []

        def generator(idx, cur):
            if idx == N:
                subset.append(list(cur))
                return
            
            cur.append(nums[idx])
            generator(idx+1, cur)
            
            cur.pop()
            generator(idx+1, cur)
            
            return
        generator(0, [])

        for i in range(len(subset)):
            cnt = len(subset[i])
            temp = 0
            for j in range(cnt):
                temp ^= subset[i][j]
            res += temp
        return res
    

    def subsetXORSum(self, nums: list[int]) -> int:
        N = len(nums)

        def xorSum(idx, cur):
            if idx == N:
                return cur
            
            withNum = xorSum(idx+1, nums[idx] ^ cur)
            withoutNum = xorSum(idx+1, cur)
            return withNum + withoutNum
        
        return xorSum(0, 0)
    
    def subsetXORSum(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            res |= nums[i]
        
        return res << (N-1)


print(Solution().subsetXORSum([1,3]))
print(Solution().subsetXORSum([5,1,6]))
print(Solution().subsetXORSum([3,4,5,6,7,8]))