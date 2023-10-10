import bisect

class Solution:
    def minOperations(self, nums:list[int]) -> int:
        allCount = len(nums)
        numsList = sorted(set(nums))
        N = len(numsList)
        ans = allCount

        def bs(target):
            l = 0
            r = N

            while l < r:
                m = l + ((r-l) >> 1)
                if numsList[m] <= target:
                    l = m + 1
                else:
                    r = m
            # print(l, r)
            return r
        
        # print("--------")
        for i, left in enumerate(numsList):
            right = left + allCount - 1
            j = bs(right)
            # j = bisect.bisect_right(numsList, right)
            ans = min(ans, allCount - (j-i))

        return ans
    

    def minOperations(self, nums):
        N = len(nums)
        allNums = sorted(set(nums))
        ans = N

        j = 0

        for i, left in enumerate(allNums):
            right = left + N - 1

            while j < len(allNums) and allNums[j] <= right:
                j += 1

            count = j - i
            ans = min(ans, N - count)

        return ans
    

    def minOperations(self, nums: list[int]) -> int:
        
        n = len(nums)
        arr = sorted(set(nums))

        j = 0
        for item in arr:
            j += item - arr[j] > n-1

        return j + n - len(arr)


    

print(Solution().minOperations([41,33,29,33,35,26,47,24,18,28]))
print(Solution().minOperations([4,2,5,3]))
print(Solution().minOperations([1,2,3,5,6]))
print(Solution().minOperations([1,10,100,1000]))
