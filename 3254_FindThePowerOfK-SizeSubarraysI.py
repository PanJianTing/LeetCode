class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        N = len(nums)
        ans = []

        for i in range(k, N+1):
            cur_sub = nums[i-k:i]
            valide = True
            for j in range(1, k):
                if not (cur_sub[j-1] < cur_sub[j] and (cur_sub[j] - cur_sub[j-1]) == 1):
                    valide = False
                    break
            if valide:
                ans.append(cur_sub[-1])
            else:
                ans.append(-1)
        
        return ans
    

print(Solution().resultsArray([1,2,3,4,3,2,5], 3))


        