from collections import defaultdict
from collections import Counter
import heapq
import random

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cntMap = defaultdict(int)

        for num in nums:
            cntMap[num] += 1

        sortedList = sorted(cntMap.items(), key=lambda x: x[1], reverse=True)
        ans = []

        for i in range(k):
            ans.append(sortedList[i][0])
        

        return ans
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == k:
            return nums
        
        cnt = Counter(nums)

        return heapq.nlargest(k, cnt, key=cnt.get)
    
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        keyList = list(cnt.keys())

        def partition(left, right, pivot_idx) -> int:
            pivot_f = cnt[keyList[pivot_idx]]

            keyList[pivot_idx], keyList[right] = keyList[right], keyList[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if cnt[keyList[i]] < pivot_f:
                    keyList[store_idx], keyList[i] = keyList[i], keyList[store_idx]
                    store_idx += 1

            keyList[right], keyList[store_idx] = keyList[store_idx], keyList[right]

            return store_idx
        
        def quickselect(left, right, k_smallest) -> None:

            if left == right:
                return
            
            pivot_idx = random.randint(left, right)

            pivot_idx = partition(left, right, pivot_idx)

            if k_smallest == pivot_idx:
                return
            
            elif k_smallest < pivot_idx:
                quickselect(left, pivot_idx-1, k_smallest)
            else:
                quickselect(pivot_idx+1, right, k_smallest)

            return
        
        n = len(keyList)
        quickselect(0, n-1, n-k)
        return keyList[n-k:]
    

class Solution:
    def topKFrequent(self, A: list[int], k: int) -> list[int]:

        if len(A) == k:
            return A

        cnt = Counter(A)

        intList = [[] for i in range(len(A) + 1)]

        for key, f in cnt.items():
            print(key, f)
            intList[f].append(key)

        ans = []
        for f in range(len(intList)-1, -1, -1):
            for key in intList[f]:
                ans.append(key)
                if len(ans) == k:
                    return ans

        return ans

print(Solution().topKFrequent([1,1,1,2,2,3], 2))

