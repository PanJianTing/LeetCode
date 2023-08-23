from collections import defaultdict
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s):
        ans = []
        cntMap = defaultdict(int)
        hq = []
        for c in s:
            cntMap[c] += 1

        for k,v in cntMap.items():
            heapq.heappush(hq, (-v, k))
        
        while hq:
            val, first_char = heapq.heappop(hq)
            if len(ans) == 0 or ans[-1] != first_char:
                ans.append(first_char)
                val += 1
                if val != 0:
                    heapq.heappush(hq, (val, first_char))
            else:
                if len(hq) == 0:
                    return ""
                second_val, second_char = heapq.heappop(hq)
                ans.append(second_char)
                second_val += 1
                if second_val != 0:
                    heapq.heappush(hq, (second_val, second_char))
                heapq.heappush(hq, (val, first_char))

        return "".join(ans)
    
    def reorganizeString(self, s):
        ans = []
        hq = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(hq)

        while hq:
            val, first_char = heapq.heappop(hq)
            if len(ans) == 0 or ans[-1] != first_char:
                ans.append(first_char)
                val += 1
                if val != 0:
                    heapq.heappush(hq, (val, first_char))
            else:
                if len(hq) == 0:
                    return ""
                second_val, second_char = heapq.heappop(hq)
                ans.append(second_char)
                second_val += 1
                if second_val != 0:
                    heapq.heappush(hq, (second_val, second_char))
                heapq.heappush(hq, (val, first_char))

        return "".join(ans)
    
    def reorganizeString(self, s):
        
        N = len(s)
        cnt_map = defaultdict(int)
        for c in s:
            cnt_map[c] += 1

        max_letter, max_cnt = "", 0

        for k, v in cnt_map.items():
            if v > max_cnt:
                max_letter = k
                max_cnt = v
        
        if ((max_cnt << 1) - 1) > N:
            return ""
        
        idx = 0
        ans = [""] * N

        while cnt_map[max_letter] > 0:
            ans[idx] = max_letter
            cnt_map[max_letter] -= 1
            idx += 2
        
        for k, v in cnt_map.items():
            while v > 0:
                if idx >= N:
                    idx = 1
                ans[idx] = k
                v -= 1
                idx += 2
        return "".join(ans)
    
    def reorganizeString(self, s):
        res, c = [], Counter(s)
        pq = [(-v, k) for k, v in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            # 代表還有
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = ''.join(res)
        if len(res) != len(s):
            return ""
        return res

# print(Solution().reorganizeString("aab"))
# print(Solution().reorganizeString("aaab"))
print(Solution().reorganizeString("aaabbc"))
# print(Solution().reorganizeString("vvvlo"))
# print(Solution().reorganizeString("baaba"))

        