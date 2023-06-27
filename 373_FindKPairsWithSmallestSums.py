import heapq
from itertools import product
from itertools import islice

class Solution:
    def kSmallestPairs(self, nums1, nums2, k) -> list[list[int]]:

        ans = []
        N = len(nums1)
        M = len(nums2)
        for i in range(N):
            for j in range(M):
                ans.append([nums1[i], nums2[j]])

        ans = sorted(ans, key=lambda x: x[0]+x[1])
        return ans[:k]
    
    def kSmallestPairs(self, nums1, nums2, k) -> list[list[int]]:

        hq = []
        M = len(nums1)
        N = len(nums2)
        k = min(k, M*N)
        ans = []
        visit = set()

        heapq.heappush(hq, (nums1[0]+ nums2[0], 0, 0))
        visit.add((0,0))

        for _ in range(k):
            _, i, j = heapq.heappop(hq)
            
            ans.append([nums1[i], nums2[j]])

            if i+1 < M and (i+1, j) not in visit:
                # print(i+1, j)
                heapq.heappush(hq, (nums1[i+1]+nums2[j], i+1, j))
                visit.add((i+1, j))
            
            if j+1 < N and (i, j+1) not in visit:
                # print(i, j+1)
                heapq.heappush(hq, (nums1[i]+nums2[j+1], i, j+1))
                visit.add((i, j+1))

        return ans
    

    def kSmallestPairs(self, num1, num2, k):
        return sorted(product(num1, num2), key=sum)[:k]
    
    def kSmallestPairs(self, nums1, nums2, k):
        return map(list, sorted(product(nums1, nums2), key=sum)[:k])
    
    def kSmallestPairs(self, nums1, nums2, k):
        return map(list, heapq.nsmallest(k, product(nums1, nums2), key=sum))
    

    def kSmallestPairs(self, nums1, nums2, k):
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        streams = heapq.merge(*streams)
        return [suv[1:] for suv in islice(streams, k)]
    

    def kSmallestPairs(self, nums1, nums2, k) -> list[list[int]]:

        hq = []
        M = len(nums1)
        N = len(nums2)
        k = min(k, M*N)
        ans = []

        heapq.heappush(hq, (nums1[0]+ nums2[0], 0, 0))

        for _ in range(k):
            _, i, j = heapq.heappop(hq)
            
            ans.append([nums1[i], nums2[j]])

            if i+1 < M and j == 0:
                heapq.heappush(hq, (nums1[i+1]+nums2[j], i+1, j))
            
            if j+1 < N:
                heapq.heappush(hq, (nums1[i]+nums2[j+1], i, j+1))

        return ans



        
                
print(Solution().kSmallestPairs([1,7,11], [2,4,6], 3))
print(Solution().kSmallestPairs([1,1,2], [1,2,3], 2))
print(Solution().kSmallestPairs([1,2], [3], 3))
print(Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 10))


