class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list[list[int]]:
        N = len(candidates)
        candidates.sort()
        self.res = []
        self.cur_list = []

        def dp(idx, cur_sum):
            if cur_sum == target:
                self.res.append(self.cur_list[:])
                return

            if cur_sum > target or idx == N:
                return
            
            for next_idx in range(idx, N):
                if next_idx > idx and candidates[next_idx-1] == candidates[next_idx]:
                    continue

                self.cur_list.append(candidates[next_idx])
                dp(next_idx+1, cur_sum + candidates[next_idx])
                self.cur_list.pop()

        self.cur_list = []
        dp(0, 0)

        return self.res
    

    def combinationSum2(self, candidates: list, target: int) -> list[list[int]]:
        N = len(candidates)
        candidates.sort()
        self.res = []

        def dp(idx, cur_sum, cur_list):
            if cur_sum == target:
                self.res.append(cur_list)
                return
            
            if idx == N or cur_sum > target:
                return
        
            for i in range(idx, N):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dp(i+1, cur_sum+candidates[i], cur_list + [candidates[i]])

        dp(0, 0, [])            
        
        return self.res

    
print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
print(Solution().combinationSum2([2,5,2,1,2], 5))
