class Solution:
    def permute(self, nums) -> list[list[int]]:

        N = len(nums)
        ans = [[]]

        for _ in range(0, N):
            temp = []
            for t in ans:
                tempNums = []

                for n in nums:
                    if n not in t:
                        tempNums.append(n)
                
                for n in tempNums:
                    temp.append([n]+ t)

            ans = temp
        return ans
    
    def permute(self, nums) -> list[list[int]]:

        N = len(nums)

        if N == 1:
            return [nums[:]]
        
        ans = []
        for n in nums:
            nextNums = []
            for ne in nums:
                if not (ne == n):
                    nextNums.append(ne)

            temp = self.permute(nextNums)
            for t in temp:
                ans.append([n] + t)
        return ans
    
    def permute(self, nums) -> list[list[int]]:

        ans = []
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()
        backtrack([])
        return ans
    
print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))
                



