from collections import defaultdict
import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:

        pair = [(i, j) for i, j in zip(nums1, nums2)]
        pair = sorted(pair, key = lambda x : x[1], reverse=True)

        top_k_heap = [x[0] for x in pair[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        ans = top_k_sum * pair[k-1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pair[i][0]
            heapq.heappush(top_k_heap, pair[i][0])

            ans = max(ans, top_k_sum * pair[i][1])

        return ans
    

    def maxScore(self, A: list[int], B: list[int], k: int) -> int:

        total = res = 0
        h = []
        pairs = sorted(list(zip(A, B)), key= lambda ab: ab[1], reverse=True)

        for a, b in pairs:
            heapq.heappush(h, a)
            total += a
            if len(h) > k:
                total -= heapq.heappop(h)
            if len(h) == k:
                res = max(res, total * b)
        return res


    







print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))
print(Solution().maxScore([4,2,3,1,1], [7,5,10,9,6], 1))
print(Solution().maxScore([2,1,14,12], [11,7,13,6], 3))


        
