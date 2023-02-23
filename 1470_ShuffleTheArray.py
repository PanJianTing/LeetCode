class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        i = 0
        while i < n:
            res.append(nums[i])
            res.append(nums[i+n])
            i += 1

        return res

    def shuffle(self, nums: list[int], n: int) -> list[int]:
        
        base = 1023
        for i in range(0, n):
            nums[i] = (nums[i] << 10) | nums[i+n]

        for i in range(n-1, -1, -1):
            first = nums[i] >> 10
            second = (nums[i] & base)
            nums[i*2] = first
            nums[i*2 + 1] = second
        return  nums


print(Solution().shuffle([2,5,1,3,4,7], 3))
print(Solution().shuffle([1,2,3,4,4,3,2,1], 4))
print(Solution().shuffle([1,1,2,2], 2))