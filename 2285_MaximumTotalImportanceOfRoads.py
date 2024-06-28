from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        cnt_map = defaultdict(int)
        important_list = [0] * n
        res = 0

        for u, v in roads:
            cnt_map[u] += 1
            cnt_map[v] += 1
        
        max_map = defaultdict(list)

        for k in cnt_map.keys():
            max_map[cnt_map[k]].append(k)
        
        score = n
        for k in sorted(max_map.keys(), reverse=True):
            for city in max_map[k]:
                important_list[city] = score
                score -= 1
        
        for u, v in roads:
            res += important_list[u] + important_list[v]
        
        return res
    
    def maximumImportance(self, N: int, roads: list[list[int]]) -> int:
        cnt_list = [0] * N
        res = 0

        for u, v in roads:
            cnt_list[u] += 1
            cnt_list[v] += 1

        cnt_list.sort()

        for i in range(N) :
            res += ((i+1) * cnt_list[i])
        
        return res
        
    
print(Solution().maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
        


