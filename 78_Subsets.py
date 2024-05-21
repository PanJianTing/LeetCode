class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for n in nums:
            subset_cnt = len(res)
            for i in range(subset_cnt):
                cur = res[i]
                res.append(cur + [n])
        return res
    
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        N = len(nums)

        def backtrack(idx, cur):
            if idx == N:
                res.append(list(cur))
                return
            
            cur.append(nums[idx])
            backtrack(idx+1, cur)
            cur.pop()
            backtrack(idx+1, cur)
            return 
        backtrack(0, [])
        return res
    

    def subsets(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        res = []
        bitmask = 1 << N
        
        for i in range(2**N):
            mask = bin(bitmask | i)[3:]
            temp = []
            for j in range(N):
                if mask[j] == '1':
                    temp.append(nums[j])
            res.append(temp)
        
        return res
    
    def subsets(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        res = []
        
        for i in range(2**N, 2**(N+1)):
            mask = bin(i)[3:]
            temp = []
            for j in range(N):
                if mask[j] == '1':
                    temp.append(nums[j])
            res.append(temp)
        
        return res


print(Solution().subsets([1,2,3]))
