class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        M = len(nums1)
        N = len(nums2)
        res = 0

        for i in range(M):
            for j in range(N):
                if (nums1[i] % (nums2[j] * k)) == 0:
                    res += 1
        return res
