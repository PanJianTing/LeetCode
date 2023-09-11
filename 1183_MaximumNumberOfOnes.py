class Solution:
    def maximumNumberOfOnes(self, w, h, sl, maxOnes):
        count = []

        for r in range(0, sl):
            for c in range(0, sl):
                totalW = 1 + (w - (r + 1)) // sl
                totalH = 1 + (h - (c + 1)) // sl
                count.append(totalW * totalH)
                # count.append((1 + (w - 1 - c) // sl) * (1 + (h - r - 1) // sl))
        count.sort(reverse=True)

        return sum(count[:maxOnes])
    
print(Solution().maximumNumberOfOnes(3, 3, 2, 1))
print(Solution().maximumNumberOfOnes(3, 3, 2, 2))
print(Solution().maximumNumberOfOnes(7, 8, 3, 3))

