class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res = []

        for q in queries:
            q_res = True
            for i in range(q[0], q[1]):
                if nums[i] % 2 == nums[i+1] % 2:
                    q_res = False
                    break
            res.append(q_res)
            
        return res
    
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        N = len(nums)
        valid_pairs = [1] * (N-1)
        prefix_pairs = [0] * N
        res = []

        for i in range(N-1):
            if nums[i] % 2 == nums[i+1] % 2:
                valid_pairs[i] = 0
            else:
                valid_pairs[i] = 1
        
        for i in range(1, N):
            prefix_pairs[i] = prefix_pairs[i-1] + valid_pairs[i-1]
        
        for st, end in queries:
            if prefix_pairs[end] - prefix_pairs[st] == end - st:
                res.append(True)
            else:
                res.append(False)
        return res
        


print(Solution().isArraySpecial([3,4,1,2,6], [[0,4]]))
print(Solution().isArraySpecial([4,3,1,6], [[0,2],[2,3]]))