from collections import defaultdict

class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        N = len(items)
        ans = []
        cur_beauty = 0
        cur_idx = 0
        items.sort()
        sort_queries = sorted(queries)
        q_to_b = defaultdict(int)
        
        for q in sort_queries:

            while cur_idx < N and items[cur_idx][0] <= q:
                cur_beauty = max(cur_beauty, items[cur_idx][1])
                cur_idx += 1
            
            q_to_b[q] = cur_beauty
        
        for q in queries:
            ans.append(q_to_b[q])
        return ans
    

    def maximumBeauty(self, nums: list[list[int]], queries: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()
        ans = []

        for i in range(1, N):
            nums[i][1] = max(nums[i-1][1], nums[i][1])

        def bs(target):
            l = 0
            r = N-1
            res = 0

            while l <= r:
                m = l + ((r-l) >> 1)
                if nums[m][0] > target:
                    r = m-1
                else:
                    res = max(res, nums[m][1])
                    l = m + 1
            
            return res
        
        for q in queries:
            ans.append(bs(q))
        
        return ans
    

    def maximumBeauty(self, nums: list[list[int]], queries: list[int]) -> list[int]:
        N = len(nums)
        ans = [0] * len(queries)
        queries_idx = [[0] * 2 for _ in range(len(queries))]

        nums.sort()

        for i, q in enumerate(queries):
            queries_idx[i][0] = q
            queries_idx[i][1] = i

        queries_idx.sort()
        cur_idx = 0
        cur_beauty = 0

        for cur_q, origin_idx in queries_idx:

            while cur_idx < N and nums[cur_idx][0] <= cur_q:
                cur_beauty = max(cur_beauty, nums[cur_idx][1])
                cur_idx += 1

            ans[origin_idx] = cur_beauty

        return ans

print(Solution().maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]))
            
        