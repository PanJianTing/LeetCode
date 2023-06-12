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
    
class Solution:
    def summaryRanges(self, A) -> list[str]:

        if len(A) == 0:
            return []

        ans = []
        temp = []
        temp.append(A[0])

        for i in range(1, len(A)):
            num = A[i]
            if num - temp[-1] == 1:
                temp.append(num)
            else:
                if len(temp) == 1:
                    ans.append(str(temp[0]))
                else:
                    ans.append(str(temp[0]) + "->" + str(temp[-1]))
                temp = []
                temp.append(num)

        if len(temp) == 1:
             ans.append(str(temp[0]))
        else:
            ans.append(str(temp[0]) + "->" + str(temp[-1]))

        return ans
    
    def summaryRanges(self, A):

        i, j, res = 0, 0, []
        N = len(A)

        while i < N and j < N:
            if j+1 < N and A[j+1] == A[j] + 1:
                j += 1
            else:
                if i == j:
                    res.append(str(A[i]))
                    
                else:
                    res.append(str(A[i]) + "->" + str(A[j]))
                    
                i = j+1
                j += 1

        return res
    
    def summaryRanges(self ,A):

        res = []
        N = len(A)
        i = 0
        while i < N:
            st = A[i]

            while i + 1 < N and A[i]+1 == A[i+1]:
                i += 1

            if st == A[i]:
                res.append(str(A[i]))
            else:
                res.append(str(st) + "->" + str(A[i]))
            
            i += 1

            
        return res




print(Solution().summaryRanges([0,1,2,4,5,7]))