class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        sortArr = sorted(set(arr))
        rankMap = {}

        rank = []

        for i, count in enumerate(sortArr):

            rankMap[count] = i + 1

        for count in arr:
            rank.append(rankMap[count])


        return rank
    
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        N = len(arr)
        sort_array = sorted(arr)
        res = []
        rank_map = {}
        rank = 1

        for n in sort_array:
            if n not in rank_map:
                rank_map[n] = rank
                rank += 1
        
        for n in arr:
            res.append(rank_map[n])

        return res
    

    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        N = len(arr)
        res = []
        rank_map = {}
        sort_arr = sorted(arr)
        rank = 1
        
        for i in range(N):
            if i > 0 and sort_arr[i] > sort_arr[i-1]:
                rank += 1
            rank_map[sort_arr[i]] = rank

        for n in arr:
            res.append(rank_map[n])

        return res
    
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        N = len(arr)
        sort_arr = sorted(set(arr))
        rank = 1
        rank_map = {}
        res = []

        for n in sort_arr:
            rank_map[n] = rank
            rank += 1
        
        for n in arr:
            res.append(rank_map[n])

        return res
    
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        N = len(arr)
        idx_map = {k: [] for k in sorted(set(arr))}

        for i, n in enumerate(arr):
            idx_map[n].append(i)

        rank = 1
        for n in idx_map.keys():
            for idx in idx_map[n]:
                arr[idx] = rank
            rank += 1
        
        return arr
            



    
print(Solution().arrayRankTransform([40,10,20,30]))