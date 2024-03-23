class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            for j in range(i, N):
                cnt_zero = 0
                cnt_ones = 0
                for k in range(i, j+1):
                    if nums[k]:
                        cnt_ones += 1
                    else:
                        cnt_zero += 1
                if cnt_zero == cnt_ones:
                    ans = max(ans, j-i+1)
        return ans
    
    def findMaxLength(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        for st in range(N):
            cnt_zero = 0
            cnt_ones = 0

            for end in range(st, N):
                if nums[end]:
                    cnt_ones += 1
                else:
                    cnt_zero += 1

                if cnt_ones == cnt_zero:
                    ans = max(ans, end-st+1)

        return ans
    
    def findMaxLength(self, nums: list[int]) -> int:
        N = len(nums)
        arr = [None] * (2*N+1)
        arr[N] = -1
        ans = 0
        cnt = 0
        for i in range(N):
            cnt += 1 if (nums[i] == 1) else -1
            if arr[cnt + N] != None:
                ans = max(ans, i - arr[cnt + N])
            else:
                arr[cnt + N] = i
        return ans
    
    def findMaxLength(self, nums: list[int]) -> int:
        cnt_map = {}
        ans = 0
        cnt = 0
        cnt_map[0] = -1

        for i, n in enumerate(nums):
            cnt += 1 if n else -1
            if cnt in cnt_map:
                ans = max(ans, i - cnt_map[cnt])
            else:
                cnt_map[cnt] = i
        
        return ans
        
    

print(Solution().findMaxLength([0,1]))
print(Solution().findMaxLength([0,1,0]))
print(Solution().findMaxLength([0,0,0,1,1,1]))
print(Solution().findMaxLength([0,1,0,1,0,1]))

