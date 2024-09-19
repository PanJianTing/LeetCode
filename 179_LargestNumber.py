class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        string_nums = []

        for n in nums:
            string_nums.append(str(n))

        string_nums.sort(key=lambda a: a * 10, reverse=True)

        if string_nums[0] == "0":
            return "0"

        return "".join(string_nums)
    
print(Solution().largestNumber([10,2]))