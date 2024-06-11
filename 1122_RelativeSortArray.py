from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        cnt_map = defaultdict(int)
        res = []

        for n in arr1:
            cnt_map[n] += 1
        
        for n in arr2:
            res += [n] * cnt_map[n]
            cnt_map[n] = 0
        
        for n in sorted(cnt_map.keys()):
            if cnt_map[n]:
                res += [n] * cnt_map[n]

        return res
    
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = []
        N = len(arr1)

        for n in arr2:
            for i in range(N):
                if n == arr1[i]:
                    res.append(n)
                    arr1[i] = -1
        arr1.sort()
        for n in arr1:
            if n != -1:
                res.append(n)

        return res
    
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        cnt_map = defaultdict(int)
        arr2_set = set(arr2)
        remaing_list = []
        res = []

        for n in arr1:
            if n in arr2_set:
                cnt_map[n] += 1
            else:
                remaing_list.append(n)

        remaing_list.sort()

        for n in arr2:
            res += [n] * cnt_map[n]
        
        return res + remaing_list
    
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        max_num = max(arr1)
        cnt_list = [0] * (max_num+1)
        res = []

        for n in arr1:
            cnt_list[n] += 1
        
        for n in arr2:
            while cnt_list[n] > 0:
                res.append(n)
                cnt_list[n] -= 1
        
        for i in range(max_num+1):
            while cnt_list[i]:
                res.append(i)
                cnt_list[i] -= 1
        
        return res

                
    
print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(Solution().relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
