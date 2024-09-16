class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        N = len(timePoints)
        min_list = []

        for t in timePoints:
            h, m = t.split(':')[0], t.split(':')[1]
            min_list.append(int(h) * 60 + int(m))

        min_list.sort()

        res = min_list[0] + 1440 - min_list[-1]

        for i in range(1, N):
            res = min(res, min_list[i] - min_list[i-1])
        
        return res
    

    def findMinDifference(self, timePoints: list[str]) -> int:
        MAX = 24 * 60
        N = len(timePoints)
        min_list = [False] * MAX

        for t in timePoints:
            h, m = t.split(':')[0], t.split(':')[1]
            idx = int(h) * 60 + int(m)
            if min_list[idx]:
                return 0
            else:
                min_list[idx] = True

        pre_idx = MAX
        first_idx = MAX
        last_idx = MAX
        ans = MAX

        for i in range(24 * 60):
            if min_list[i]:
                if not pre_idx == MAX:
                    ans = min(ans, i - pre_idx)
                pre_idx = i
                if first_idx == MAX:
                    first_idx = i
                last_idx = i
        
        return min(ans, first_idx + MAX - last_idx)