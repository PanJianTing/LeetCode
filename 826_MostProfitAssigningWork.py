import bisect

class Solution:
    def maxProfitAssignment(self, diff: list[int], profit: list[int], worker: list[int]) -> int:
        profit_list = []
        res = 0
        worker.sort()

        for d, p in zip(diff, profit):
            profit_list.append((d, p))

        profit_list.sort()
        idx = 0
        max_profit = 0

        for w in worker:
            
            while idx < len(profit_list) and profit_list[idx][0] <= w:
                max_profit = max(max_profit, profit_list[idx][1])
                idx += 1
            
            res += max_profit

        return res


    def maxProfitAssignment(self, diff: list[int], profit: list[int], worker: list[int]) -> int:
        profit_list = sorted(zip(diff, profit))
        res = idx = max_profit = 0
        worker.sort()
        for w in worker:
            
            while idx < len(profit_list) and profit_list[idx][0] <= w:
                max_profit = max(max_profit, profit_list[idx][1])
                idx += 1
            
            res += max_profit

        return res
    
    def maxProfitAssignment(self, diff: list[int], profit: list[int], worker: list[int]) -> int:
        N = len(diff)
        profit_list = sorted(zip(diff, profit))
        res = 0
        diff.sort()
        
        for i in range(1, N):
            profit_list[i] = (profit_list[i][0], max(profit_list[i-1][1] ,profit_list[i][1]))

        for w in worker:
            
            l = 0
            r = N-1
            max_profit = 0

            while l <= r:
                m = l + ((r-l) >> 1)
                if profit_list[m][0] <= w:
                    max_profit = max(max_profit, profit_list[m][1])
                    l = m + 1
                else:
                    r = m - 1
            
            res += max_profit
        
        return res
    
    def maxProfitAssignment(self, diff: list[int], profit: list[int], worker: list[int]) -> int:
        N = len(diff)
        profit_list = sorted(zip(profit, diff), reverse=True)
        res = 0
        
        for i in range(1, N):
            profit_list[i] = (profit_list[i][0], min(profit_list[i-1][1] ,profit_list[i][1]))

        for w in worker:
            
            l = 0
            r = N-1
            max_profit = 0

            while l <= r:
                m = l + ((r-l) >> 1)
                if profit_list[m][1] <= w:
                    max_profit = max(max_profit, profit_list[m][0])
                    r = m - 1
                else:
                    l = m + 1
            
            res += max_profit
        
        return res
    

    def maxProfitAssignment(self, diff: list[int], profit: list[int], worker: list[int]) -> int:
        max_diff = max(worker)
        profit_list = [0] * (max_diff + 1)
        res = 0

        for d, p in zip(diff, profit):
            if d > max_diff:
                continue
            profit_list[d] = max(profit_list[d], p)
        
        for i in range(1, max_diff+1):
            profit_list[i] = max(profit_list[i-1], profit_list[i])
        
        for w in worker:
            res += profit_list[w]

        return res

print(Solution().maxProfitAssignment([13,37,58], [4,90,96], [34,73,45])) #190
print(Solution().maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7])) #100
print(Solution().maxProfitAssignment([85,47,57], [24,66,99], [40,25,25])) #0

