from collections import defaultdict
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt_map = defaultdict(int)
        cnt_list = []
        ans = ""

        for c in s:
            cnt_map[c] += 1
        
        for c, cnt in cnt_map.items():
            heapq.heappush(cnt_list, (-cnt, c))
        
        while cnt_list:
            cnt, c = heapq.heappop(cnt_list)
            ans += c * (-cnt)
        return ans
    
    def frequencySort(self, s: str) -> str:
        cnt_map = defaultdict(int)
        ans = ""

        for c in s:
            cnt_map[c] += 1
        
        cnt_list = sorted(cnt_map.items(), key=lambda x : -x[1])
        for k, cnt in cnt_list:
            ans += k * cnt
        
        return ans
    
    def frequencySort(self, s: str) -> str:
        cnt_map = defaultdict(int)
        ans = []

        for c in s:
            cnt_map[c] += 1
        
        cnt_list = sorted(cnt_map.items(), key=lambda x : -x[1])
        for k, cnt in cnt_list:
            ans.append(k * cnt)
        
        return "".join(ans)
    
    def frequencySort(self, s: str) -> str:
        cnt_map = defaultdict(int)
        cnt_list = []
        ans = []

        for c in s:
            cnt_map[c] += 1
        
        for c, cnt in cnt_map.items():
            heapq.heappush(cnt_list, (-cnt, c))
        
        while cnt_list:
            cnt, c = heapq.heappop(cnt_list)
            ans.append(c * (-cnt))
        return "".join(ans)
    
    def frequencySort(self, s: str) -> str:
        if s == "":
            return ""
        
        char_list = list(s)
        group_list = []

        char_list.sort()
        char_list.append(" ")
        temp_list = [char_list[0]]

        N = len(char_list)

        for i in range(1, N):
            if temp_list[-1] != char_list[i]:
                group_list.append("".join(temp_list))
                temp_list = []
            temp_list.append(char_list[i])
        
        group_list.sort(key=lambda x: -len(x))
        return "".join(group_list)
    

    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = []

        for c, cnt in cnt.most_common():
            ans.append(cnt * c)
        
        return "".join(ans)
    
    def frequencySort(self, s: str) -> str:
        cnt_map = defaultdict(int)
        char_map = defaultdict(list)
        ans = []

        for c in s:
            cnt_map[c] += 1
        
        for char in sorted(cnt_map.keys()):
            char_map[cnt_map[char]].append(char)
        
        all_cnt_list = sorted(char_map.keys(), reverse=True)

        for cnt in all_cnt_list:
            for c in char_map[cnt]:
                ans.append(cnt * c)
        return "".join(ans)
        



        
    
print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("Aabb"))
print(Solution().frequencySort("raaeaedere"))
