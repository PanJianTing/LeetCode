from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        M = len(nums1)
        N = len(nums2)
        res = 0
        cnt_dict = defaultdict(int)
        max_cnt = max(nums1)

        for i in range(M):
            cnt_dict[nums1[i]] += 1

        multiple_nums2 = list(nums2)

        for i in range(N):
            multiple_nums2[i] = nums2[i] * k
        

        for i in range(N):
            if multiple_nums2[i] == 1:
                res += M
            else:
                temp = multiple_nums2[i]
                times = 1
                cur = temp * times
                while cur <= max_cnt:
                    if cur in cnt_dict:
                        res += cnt_dict[cur]
                    times += 1
                    cur = temp * times
        return res
    
print(Solution().numberOfPairs([1,3,4], [1,3,4], 1)) #5
print(Solution().numberOfPairs([1,2,4,12], [2,4], 3)) #2
print(Solution().numberOfPairs([12,4], [1,4], 3)) #2
