from collections import defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        hq = []
        cnt_map = defaultdict(int)
        time = 0

        for t in tasks:
            cnt_map[t] += 1
        
        for key in cnt_map:
            heapq.heappush(hq, cnt_map[key] * -1)

        while hq:
            cycle = n+1
            exe_task = []
            task_cnt = 0

            while cycle > 0 and hq:
                cnt = heapq.heappop(hq)
                cnt += 1
                if cnt < 0:
                    exe_task.append(cnt)
                task_cnt += 1
                cycle -= 1
            
            for x in exe_task:
                heapq.heappush(hq, x)
            
            time += n+1 if hq else task_cnt
        return time
    
    def leastInterval(self, tasks: list[int], n: int) -> int:
        cnt_list = [0] * 26

        for t in tasks:
            cnt_list[ord(t) - ord('A')] += 1

        cnt_list.sort()
        slot = (cnt_list[-1] - 1) * n

        for i in range(24, -1, -1):
            if cnt_list[i] > 0:
                slot -= cnt_list[i]
                if cnt_list[-1] == cnt_list[i]:
                    slot += 1
        return slot + len(tasks) if slot > 0 else len(tasks)

    def leastInterval(self, tasks: list[int], n: int) -> int:
        N = len(tasks)
        cnt_list = [0] * 26
        max_freq = 0
        max_cnt = 0

        for t in tasks:
            cnt_list[ord(t) - ord('A')] += 1

        for cnt in cnt_list:
            if cnt > max_freq:
                max_freq = cnt
                max_cnt = 1
            elif cnt == max_freq:
                max_cnt += 1
            
        slot = (n - (max_cnt-1)) * ((max_freq - 1))
        leave_slot = max(0, slot - (N - (max_cnt * max_freq)))

        return leave_slot + N
    
    def leastInterval(self, tasks: list[int], n: int) -> int:
        cnt_list = [0] * 26
        max_freq = 0
        max_cnt = 0

        for t in tasks:
            cnt_list[ord(t) - ord('A')] += 1
        
        for cnt in cnt_list:
            if cnt > max_freq:
                max_freq = cnt
                max_cnt = 1
            elif cnt == max_freq:
                max_cnt += 1
        
        return max(len(tasks), (n+1) * (max_freq-1) + max_cnt)
                



print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
print(Solution().leastInterval(["A","C","A","B","D","B"], 1))
print(Solution().leastInterval(["A","A","A","B","B","B"], 3))
print(Solution().leastInterval(["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7))