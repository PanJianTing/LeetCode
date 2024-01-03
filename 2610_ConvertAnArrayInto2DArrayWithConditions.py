from collections import defaultdict

class Solution:
    def findMatrix(self, nums) -> int:
        ans = []
        N = len(nums)
        cnt_map = defaultdict(int)
        all_set = set(nums)

        for n in nums:
            cnt_map[n] += 1
        
        for _ in range(N):
            temp = set()
            for n in all_set:
                if cnt_map[n] > 0:
                    temp.add(n)
                    cnt_map[n] -= 1
            if len(temp) > 0:
                ans.append(temp)
            
        return ans
    
    def findMatrix(self, nums) -> list[list[int]]:
        N = len(nums)
        ans = []
        idx_set = set()

        while len(idx_set) < N:
            temp = set()
            for i in range(N):
                if i not in idx_set and nums[i] not in temp:
                    temp.add(nums[i])
                    idx_set.add(i)
            ans.append(temp)
            
        return ans
    
    def findMatrix(self, nums) -> list[list[int]]:
        N = len(nums)
        ans = []

        for n in nums:
            add_new = True

            for g in ans:
                if n in g:
                    continue
                else:
                    add_new = False
                    g.add(n)
                    break
            if add_new:
                ans.append(set([n]))
            
        return ans
    
    def findMatrix(self, nums) -> list[list[int]]:
        N = len(nums)
        ans = []
        freq = [0] * (N+1)
        
        for n in nums:
            if freq[n] >= len(ans):
                ans.append([])
            ans[freq[n]].append(n)
            freq[n] += 1
        
        return ans
        

print(Solution().findMatrix([1,3,4,1,2,3,1]))
print(Solution().findMatrix([1,2,3,4]))