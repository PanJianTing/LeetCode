class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        N = len(customers)
        cur_time = 0
        waiting_time = 0

        for i in range(N):
            time, wait = customers[i]
            if cur_time <= time:
                cur_time = (time + wait)
                waiting_time += wait
            else:
                waiting_time += ((cur_time - time) + wait)
                cur_time += wait
                
        return waiting_time / N

    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        N = len(customers)
        next_idle = 0
        waiting = 0

        for cus in customers:
            next_idle = max(cus[0], next_idle) + cus[1]
            waiting += (next_idle - cus[0])
        
        return waiting / N
    

print(Solution().averageWaitingTime([[1,2],[2,5],[4,3]]))
print(Solution().averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))