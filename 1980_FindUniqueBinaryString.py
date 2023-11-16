import random

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        
        N = len(nums)
        allNums = set()

        for n in nums:
            allNums.add(int(n, 2))
        
        for n in range(0, N+1):
            if n not in allNums:
                return '{0:b}'.format(n).zfill(N)
            

    def findDifferentBinaryString(self, nums: list[str]) -> str:
        N = len(nums)
        numsSet = set(nums)

        def generate(cur):
            if len(cur) == N:
                if cur not in numsSet:
                    return cur
                
                return ""
            
            res = generate(cur + '0')
            if len(res) == 0:
                return generate(cur + '1')
            return res
        
        return generate("")
    
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        N = len(nums)
        allNums = set()

        for n in nums:
            allNums.add(int(n, 2))
        
        for i in range(N+1):
            if i not in allNums:
                return '{0:b}'.format(i).zfill(N)
            

    def findDifferentBinaryString(self, nums: list[str]) -> str:

        N = len(nums)
        allNums = set()

        for n in nums:
            allNums.add(int(n, 2))

        ans = next(iter(allNums))

        while ans in allNums:
            ans = random.randrange(0, ((2 ** N)-1))

        return '{0:b}'.format(ans).zfill(N)
    
    def findDifferentBinaryString(self, nums: list[str]) -> str:

        N = len(nums)
        ans = []

        for i in range(N):
            ans.append('1' if nums[i][i] == '0' else '0')
        
        return "".join(ans)

            

print(Solution().findDifferentBinaryString(["01","10"]))
print(Solution().findDifferentBinaryString(["00","01"]))
print(Solution().findDifferentBinaryString(["111","011","001"]))
        