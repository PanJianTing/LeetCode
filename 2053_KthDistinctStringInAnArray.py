from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        N = len(arr)
        cnt_map = defaultdict(int)

        for s in arr:
            cnt_map[s] += 1
        
        for s in arr:
            if cnt_map[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
    
    def kthDistinct(self, arr: list[str], k: int) -> str:
        N = len(arr)
        distinct_list = []

        for i in range(N):
            is_add = True
            for j in range(N):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    is_add = False
                    break
            if is_add:
                distinct_list.append(arr[i])
        
        if len(distinct_list) >= k:
            return distinct_list[k-1]
        return ''
    
    def kthDistinct(self, arr: list[str], k: int) -> str:
        distinct_set = set()
        dup_set = set()

        for s in arr:
            
            if s in dup_set:
                continue
                
            if s in distinct_set:
                distinct_set.remove(s)
                dup_set.add(s)
            else:
                distinct_set.add(s)
        
        for s in arr:
            if s in distinct_set:
                k -= 1
                if k == 0:
                    return s
                
        return ""

    
print(Solution().kthDistinct(["d","b","c","b","c","a"], 2))
print(Solution().kthDistinct(["aaa","aa","a"], 1))
print(Solution().kthDistinct(["a","b","a"], 3))