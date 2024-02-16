from collections import defaultdict
from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        N = len(arr)
        cnt_map = defaultdict(int)
        hp = []

        for num in arr:
            cnt_map[num] += 1
        
        for num in cnt_map:
            heapq.heappush(hp, (cnt_map[num], num))

        for _ in range(k):
            cur_cnt, cur_num = heapq.heappop(hp)
            cur_cnt -= 1
            if cur_cnt > 0:
                heapq.heappush(hp, (cur_cnt, cur_num))
        return len(hp)
    
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        cnt_map = defaultdict(int)

        for num in arr:
            cnt_map[num] += 1
        
        cnt_list = sorted(cnt_map.values())
        N = len(cnt_list)
        idx = 0

        while k > 0 and idx < len(cnt_list):
            cur_cnt = cnt_list[idx]
            if k >= cur_cnt:
                k -= cur_cnt
                idx += 1
            else:
                break
        return N - idx
    
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        cnt_map = Counter(arr)
        cnt_list = sorted(cnt_map.values())
        cur_remove = 0
        N = len(cnt_list)

        for i in range(N):
            cur_remove += cnt_list[i]

            if cur_remove > k:
                return N - i
        return 0
    
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        cnt_map = Counter(arr)
        cnt_list = list(cnt_map.values())
        heapq.heapify(cnt_list)
        # cur_remove = 

        while cnt_list and cnt_list[0] <= k:
            k -= heapq.heappop(cnt_list)

        return len(cnt_list)
    
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        cnt_map = Counter(arr)
        cnt_list = list(cnt_map.values())
        heapq.heapify(cnt_list)
        cur_remove = 0

        while cnt_list:
            cur_remove += heapq.heappop(cnt_list)
            if cur_remove > k:
                return len(cnt_list) + 1

        return 0
    
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        N = len(arr)
        cnt_map = Counter(arr)
        cnt_list = [0] * (N+1)
        remain_remove = k
        remain_cnt = len(cnt_map)

        for cnt in cnt_map.values():
            cnt_list[cnt] += 1
        
        for i in range(1, N+1):
            cur_remove = i * cnt_list[i]
            if remain_remove >= cur_remove:
                remain_remove -= cur_remove
                remain_cnt -= cnt_list[i]
            else:
                remain_cnt -= remain_remove // i
                remain_remove = 0

            if remain_remove <= 0:
                return remain_cnt
        return 0
    
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        N = len(arr)
        cnt_map = Counter(arr)
        cnt_list = [0] * (N+1)
        remain_remove = k
        remain_cnt = len(cnt_map)

        for cnt in cnt_map.values():
            cnt_list[cnt] += 1
        
        for i in range(1, N+1):
            count_remove = min(remain_remove // i, cnt_list[i])
            remain_remove -= (count_remove * i)
            remain_cnt -= count_remove

            if remain_remove < i:
                return remain_cnt
            
        return 0


print(Solution().findLeastNumOfUniqueInts([1], 1))
print(Solution().findLeastNumOfUniqueInts([5,5,4], 1))
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))