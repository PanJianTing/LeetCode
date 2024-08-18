import heapq

class Solution:

    def nthUglyNumber(self, N: int) -> int:
        ugly_set = set()
        ugly_set.add(1)

        cur_num = 1

        for _ in range(N):
            cur_num = min(ugly_set)
            ugly_set.remove(cur_num)

            ugly_set.add(2 * cur_num)
            ugly_set.add(3 * cur_num)
            ugly_set.add(5 * cur_num)

        return cur_num
    
    def nthUglyNumber(self, N: int) -> int:
        hq = []
        heapq.heappush(hq, 1)
        visit = set()
        visit.add(1)
        res = 1

        for _ in range(N):
            res = heapq.heappop(hq)

            for num in [2,3,5]:
                temp = res * num
                if temp not in visit:
                    heapq.heappush(hq, temp)
                    visit.add(temp)

        return res
    
    def nthUglyNumber(self, N: int) -> int:
        dp = [0] * N
        dp[0] = 1

        idx_2, idx_3, idx_5 = 0, 0, 0
        next_2, next_3, next_5 = 2, 3, 5
        
        for i in range(1, N):
            next_num = min(next_2, next_3, next_5)
            dp[i] = next_num

            if next_num == next_2:
                idx_2 += 1
                next_2 = dp[idx_2] * 2
            
            if next_num == next_3:
                idx_3 += 1
                next_3 = dp[idx_3] * 3
            
            if next_num == next_5:
                idx_5 += 1
                next_5 = dp[idx_5] * 5
            
        return dp[-1]



# print(Solution().nthUglyNumber(4))
# print(Solution().nthUglyNumber(10))
print(Solution().nthUglyNumber(11))
