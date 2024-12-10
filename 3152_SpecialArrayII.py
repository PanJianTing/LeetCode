class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        no_idx = []
        ans = []

        for i in range(1, len(nums)):
            if nums[i-1] & 1 == nums[i] & 1:
                no_idx.append(i)

        def bs(st, end):
            l = 0
            r = len(no_idx) - 1

            while l <= r:
                m = l + ((r-l) >> 1)

                if no_idx[m] < st:
                    l = m + 1
                elif no_idx[m] > end:
                    r = m - 1
                else:
                    return True
            return False

        for st, end in queries:

            if bs(st+1, end):
                ans.append(False)
            else:
                ans.append(True)
        return ans
    

print(Solution().isArraySpecial([3,4,1,2,6], [[0,4]]))
print(Solution().isArraySpecial([4,3,1,6], [[0,2],[2,3]]))




            