import heapq

class Solution:
    def rangeSum(self, nums: list[int], N: int, left: int, right: int) -> int:
        all_sum = []
        ans = 0
        
        for i in range(N):
            cur = 0
            for j in range(i, N):
                cur += nums[j]
                all_sum.append(cur)
        
        all_sum.sort()
        
        for i in range(left-1, right):
            ans += all_sum[i]
        
        return ans % (10**9 + 7)
    
    def rangeSum(self, nums: list[int], N: int, left: int, right: int) -> int:
        hq = []
        ans = 0

        for i in range(N):
            heapq.heappush(hq, (nums[i], i))

        for i in range(1, right+1):
            cur_num, cur_idx = heapq.heappop(hq)

            if i >= left:
                ans += cur_num
            
            if cur_idx < N-1:
                next_push = (cur_num + nums[cur_idx+1], cur_idx+1)
                heapq.heappush(hq, next_push)

        return ans % (10 ** 9 + 7)
    

    def rangeSum(self, nums: list[int], N: int, left: int, right: int) -> int:
        mod = 10**9 + 7

        def count_and_sum(target):
            count = 0
            cur_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(N):
                cur_sum += nums[j]
                window_sum += (nums[j] * (j-i+1))
                while cur_sum > target:
                    window_sum -= cur_sum
                    cur_sum -= nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return count, total_sum
        
        def sum_of_first_k(k):
            min_sum = min(nums)
            max_sum = sum(nums)
            l = min_sum
            r = max_sum

            while l <= r:
                m = l + ((r-l) >> 1)
                cur_cnt, cur_sum = count_and_sum(m)
                if cur_cnt >= k:
                    r = m - 1
                else:
                    l = m + 1
            cur_cnt, cur_sum = count_and_sum(l)
            return cur_sum - l * (cur_cnt - k)
        
        return (sum_of_first_k(right) - sum_of_first_k(left-1)) % mod


    
print(Solution().rangeSum([1,2,3,4], 4, 1, 5))
print(Solution().rangeSum([1,2,3,4], 4, 3, 4))
print(Solution().rangeSum([1,2,3,4], 4, 1, 10))