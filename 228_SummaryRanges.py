class Solution:

    def summaryRanges(self, nums: list[int]) -> list[str]:

        count = len(nums)

        summary = []

        i = 0

        while i < count:
            j = i
            while j < count-1:
                if nums[j+1] - nums[j] == 1:
                    j += 1
                else:
                    break
            if j == i:
                summary.append(str(nums[j]))
            else:
                summary.append(str(nums[i]) + "->" + str(nums[j]))
            i = j + 1

        return summary



    def summaryRanges_my(self, nums: list[int]) -> list[str]:

        if len(nums) == 1:
            return [str(nums[0])]

        ranges = []

        summary = []

        for i in range(len(nums)):

            rangesCount = len(ranges)

            if rangesCount == 0:
                ranges.append(nums[i])
            elif rangesCount == 1:
                if nums[i] - ranges[0] == 1:
                    ranges.append(nums[i])
                else:
                    summary.append(str(ranges[0]))
                    ranges = [nums[i]]

            elif rangesCount == 2:
                if nums[i] - ranges[1] == 1:
                    ranges[1] = nums[i]
                else:
                    summary.append(str(ranges[0]) + "->" + str(ranges[1]))
                    ranges = [nums[i]]

        if len(ranges) == 1:
            summary.append(str(ranges[0]))

        elif len(ranges) == 2:
            summary.append(str(ranges[0]) + "->" + str(ranges[1]))

        return summary

Solution.summaryRanges(Solution(), [0,1,2,4,5,7])