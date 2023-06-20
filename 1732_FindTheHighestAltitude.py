class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # N = [0] * (len(gain)+1)
        # for i, n in enumerate(gain):
        #     N[i+1] = n + N[i]

        # return max(N)

        now = 0
        maxH = 0
        for g in gain:
            now += g
            maxH = max(maxH, now)
        return maxH
