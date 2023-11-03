class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:

        N = len(target)
        cur_idx = 0
        cur_cnt = 1
        stack = []
        ans = []

        while cur_idx < N:
            if target[cur_idx] == cur_cnt:
                stack.append(cur_cnt)
                cur_idx += 1
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
            
            cur_cnt += 1
        return ans
    
    def buildArray(self, target, n) -> list[str]:

        cur = 1
        ans = []
        for num in target:
            while cur < num:
                ans.append("Push")
                ans.append("Pop")
                cur += 1
            ans.append("Push")
            cur += 1
        return ans
    
    def buildArray(self, target, n) -> list[int]:

        ans = []
        targetSet = set(target)

        for num in range(1, target[-1]+1):
            ans.append("Push")
            if num not in targetSet:
                ans.append("Pop")

        return ans
    
print(Solution().buildArray([1,3], 3))
print(Solution().buildArray([1,2,3], 3))
print(Solution().buildArray([1,2], 4))


