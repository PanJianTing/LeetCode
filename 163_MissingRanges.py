class Solution:

    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        nums = [lower - 1] + nums + [upper + 1]
        n = len(nums)
        result = []

        for i in range(1, n):
            sub = nums[i] - nums[i-1]
            
            if sub == 2:
                result.append(str(nums[i] - 1))
            elif sub > 2:
                result.append(str(nums[i-1] + 1) + "->" + str(nums[i] - 1))

        return result

    def findMissingRanges_my(self, nums: list[int], lower: int, upper: int) -> list[str]:

        if nums == []:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str[upper]]

        ranges = []

        # lower
        if nums[0] != lower:
            sub = nums[0] - lower
            if sub == 1:
                ranges.append(str(lower))
            else:
                ranges.append(str(lower + 1) + "->" + str(nums[0] - 1))

        for i in range(1, len(nums)):
            sub = nums[i] - nums[i-1]
            if sub > 1:
                if sub == 2:
                    ranges.append(str(nums[i] + 1))
                else:
                    ranges.append(str(nums[i] + 1) + "->" + str(nums[i-1] - 1))


        # upper
        if nums[-1] != upper:
            sub = upper - nums[-1]
            if sub == 1:
                ranges.append(str(upper))
            else:
                ranges.append(str(nums[-1] + 1) + "->" + str(upper - 1))
        return ranges
        
        



    # time Exceeded
    def findMissingRanges_my(self, nums: list[int], lower: int, upper: int) -> list[str]:

        ranges = []
        start = ""
        end = ""

        for n in range(lower, upper + 1):
            if n not in nums:
                if start == "":
                    start = str(n)
                else:
                    end = str(n)
            else:
                if start != "":
                    if end != "":
                        ranges.append(start + "->" + end)
                    else:
                        ranges.append(start)
                start = ""
                end = ""

        if start != "":
            if end != "":
                ranges.append(start + "->" + end)
            else:
                ranges.append(start)

        return ranges


Solution.findMissingRanges(Solution(), [0,1,3,50,75], 0, 99)