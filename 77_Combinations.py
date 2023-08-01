class Solution:

    def combine(self, n, k) -> list[list[int]]:
        if k == 0:
            return []
        
        allNums = []
        for i in range(n, 0, -1):
            allNums.append(i)

        def dp(nums, k):
            if k == 0:
                return [[]]
            
            ans = []
            for i in range(0, len(nums)):
                nowNums = nums[i+1:]
                nowN = nums[i]

                now = dp(nowNums, k-1)
                for s in now:
                    s.append(nowN)
                    ans.append(s)

            return ans
        return dp(allNums, k)
    
    def combine(self, n, k) -> list[list[int]]:

        def dp(first, k):
            if k == 0:
                return [[]]
            
            ans = []
            for num in range(first, n+1):

                now = dp(num+1, k-1)
                for s in now:
                    s.append(num)
                    ans.append(s)
            return ans
        return dp(1, k)
    
    def combine(self, n, k) -> list[list[int]]:
        ans = []

        def backtrack(now, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(now, n+1):
                curr.append(num)
                backtrack(num+1, curr)
                curr.pop()

        backtrack(1, [])
        return ans
    
    def combine(self, n, k) -> list[list[int]]:
        ans = []

        def backtrack(now, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            # need 為還可以再往下長幾層
            # remain 為[now, n]這個範圍的數量
            # avaliable 為 可以從now往後幾個，可以想成留幾個給下下層用
            need = k - len(curr)
            remain = n - now + 1
            avaliable = remain - need

            for num in range(now, now + avaliable +1):
                curr.append(num)
                backtrack(num+1, curr)
                curr.pop()

        backtrack(1, [])
        return ans
    

class Solution:

    def combine(self, n, k) -> list[list[int]]:
        com = [[]]
        for _ in range(k):
            temp = []
            for c in com:
                for i in range(1, c[0] if c else n+1):
                    temp.append([i]+c)
            com = temp
        return com
    




print(Solution().combine(4, 3))
# print(Solution().combine(4, 2))
# print(Solution().combine(1, 1))

