from collections import defaultdict
import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt_map = defaultdict(int)
        cnt_list = []
        res = 0
        time = 1
        change = 0

        for c in word:
            cnt_map[c] += 1
        
        cnt_list = sorted(cnt_map.values(), reverse=True)

        for cnt in cnt_list:
            res += cnt * time
            change += 1
            if change == 8:
                change = 0
                time += 1

        return res
    

    def minimumPushes(self, word: str) -> int:
        cnt_map = defaultdict(int)
        cnt_list = []
        res = 0

        for c in word:
            cnt_map[c] += 1
        
        cnt_list = sorted(cnt_map.values(), reverse=True)

        for i, cnt in enumerate(cnt_list):
            res += ((i >> 3) + 1) * cnt

        return res
    

    def minimumPushes(self, word: str) -> int:
        cnt_list = [0] * 26
        res = 0

        for c in word:
            cnt_list[ord(c) - ord('a')] += 1
        
        cnt_list.sort(reverse=True)

        for i, cnt in enumerate(cnt_list):
            res += ((i >> 3) + 1) * cnt

        return res
    
    def minimumPushes(self, word: str) -> int:
        cnt_list = [0] * 32
        res = 0

        for i in range(26):
            cnt_list[i] = word.count(chr(97+i))
        
        cnt_list.sort(reverse=True)

        for i in range(4):
            for j in range(8):
                res += (i+1) * cnt_list[(i << 3) + j]

        return res
    

    def minimumPushes(self, word: str) -> int:
        cnt_map = defaultdict(int)
        hq = []
        idx = 0
        ans = 0

        for c in word:
            cnt_map[c] += 1
        
        hq = [-cnt for cnt in cnt_map.values()]
        heapq.heapify(hq)
        # for k in cnt_map.keys():
        #     heapq.heappush(hq, -1 * cnt_map[k])
        
        while hq:
            cur_cnt = heapq.heappop(hq) * -1
            ans += ((idx >> 3) + 1) * cur_cnt
            idx += 1
        return ans

    
print(Solution().minimumPushes("abcde"))
print(Solution().minimumPushes("xyzxyzxyzxyz"))
print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))
        
