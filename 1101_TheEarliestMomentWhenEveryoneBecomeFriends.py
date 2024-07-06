class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        time_list = []
        logs.sort()
        res = 0
        for i in range(n):
            time_list.append([float('-inf'), i])

        def find(x):
            if time_list[x][1] == x:
                return time_list[x]
            time_list[x] = find(time_list[x][1])
            return time_list[x]
        
        def join(x, y, time):
            time_x, x = find(x)
            time_y, y = find(y)

            if x != y:
                meet_time = max(time_x, time_y, time)
                new_time = [meet_time, x]
                time_list[x] = new_time
                time_list[y] = new_time
            return
        
        for t, x, y in logs:
            join(x, y, t)
        
        cur = find(time_list[0][1])
        for t, x, in time_list:
            if t == float('-inf') or not (cur == find(x)):
                return -1
            res = max(res, t)

        return res
    

    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        group = [i for i in range(n)]
        all_groups = n
        logs.sort()

        def find(x):
            if group[x] == x:
                return x
            return find(group[x])
        
        def join(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return False

            group[y] = x
                
            return True
        
        for t, x, y in logs:
            if join(x, y):
                all_groups -= 1
            if all_groups == 1:
                return t
        
        return -1
    
print(Solution().earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6))
print(Solution().earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4))
print(Solution().earliestAcq([[7,3,1],[2,3,0],[3,2,1],[6,0,1],[0,2,0],[4,3,2]], 4))
print(Solution().earliestAcq([[9,0,3],[0,2,7],[12,3,1],[5,5,2],[3,4,5],[1,5,0],[6,2,4],[2,5,3],[7,7,3]], 8))
print(Solution().earliestAcq([[3,1,2],[1,1,5],[4,4,0],[0,3,4],[2,6,2]], 7))
                

[[0, 3, 4], [1, 1, 5], [2, 6, 2], [3, 1, 2], [4, 4, 0]]
        