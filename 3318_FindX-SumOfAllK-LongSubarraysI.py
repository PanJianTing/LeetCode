from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        N = len(nums)
        ans = []

        for i in range(N - k + 1):
            cur_list = nums[i:i+k]
            cnt_map = defaultdict(int)
            num_map = defaultdict(list)
            select_num = set()
            
            for n in cur_list:
                cnt_map[n] += 1
            
            for key, cnt in cnt_map.items():
                num_map[cnt].append(key)
            
            for cnt in sorted(num_map.keys(), reverse=True):
                for num in sorted(num_map[cnt], reverse=True):
                    if len(select_num) < x:
                        select_num.add(num)

            cur_sum = 0

            for n in cur_list:
                if n in select_num:
                    cur_sum += n

            ans.append(cur_sum)

        return ans
    


    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        N = len(nums)
        ans = []
        cnt_map = defaultdict(int)
        cur_left_idx = 0

        for i in range(N):
            cnt_map[nums[i]] += 1
            if i >= k-1:
                hq = []
                for key, val in cnt_map.items():
                    heapq.heappush(hq, (-val, -key))

                cur_sum = 0
                cur_select = 0
                while hq and cur_select < x:
                    cur_v, cur_k = heapq.heappop(hq)
                    cur_sum += cur_k * cur_v
                    cur_select += 1
                    
                ans.append(cur_sum)
                cnt_map[nums[cur_left_idx]] -= 1
                cur_left_idx += 1
            
        return ans

print(Solution().findXSum([1,1,2,2,3,4,2,3], 6, 2))        
print(Solution().findXSum([3,8,7,8,7,5], 2, 2))        
print(Solution().findXSum([9,2,2], 3, 3))        