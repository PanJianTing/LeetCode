from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        N = len(s)
        cnt_list = [0] * 26
        ans = []
        idx = 25

        for c in s:
            cnt_list[ord(c) - ord('a')] += 1
        
        while idx >= 0:
            if cnt_list[idx] == 0:
                idx -= 1
                continue
            
            cur_c = chr(idx + ord('a'))
            cnt = min(repeatLimit, cnt_list[idx])
            ans.append(cur_c * cnt)
            cnt_list[idx] -= cnt

            if cnt_list[idx] > 0:
                next_idx = idx - 1
                while next_idx >= 0 and cnt_list[next_idx] == 0:
                    next_idx -= 1
                if next_idx < 0:
                    break
                ans.append(chr(next_idx + ord('a')))
                cnt_list[next_idx] -= 1

        return ''.join(ans)

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt_list = [0] * 26
        ans = []
        idx = 25

        for c in s:
            cnt_list[ord(c) - ord('a')] += 1
        
        while idx >= 0:
            while cnt_list[idx] > 0:
                cur_c = chr(idx + ord('a'))
                cnt = min(repeatLimit, cnt_list[idx])
                ans.append(cur_c * cnt)
                cnt_list[idx] -= cnt
                if cnt_list[idx] > 0:
                    next_idx = idx-1
                    while next_idx > -1:
                        if cnt_list[next_idx] > 0:
                            next_c = chr(next_idx + ord('a'))
                            ans.append(next_c)
                            cnt_list[next_idx] -= 1
                            break
                        else:
                            next_idx -= 1
                    if next_idx < 0:
                        return ''.join(ans)
            idx -= 1
        
        return ''.join(ans)

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hq = []
        ans = []

        for key, cnt in Counter(s).items():
            heapq.heappush(hq, (-1 * ord(key), cnt))
        
        while hq:
            cur_c, cur_cnt = heapq.heappop(hq)
            cnt = min(cur_cnt, repeatLimit)
            ans.append(chr(cur_c * -1) * cnt)
            cur_cnt -= cnt

            if cur_cnt > 0 and hq:
                next_c, next_cnt = heapq.heappop(hq)
                ans.append(chr(next_c * -1))
                next_cnt -= 1
                if next_cnt > 0:
                    heapq.heappush(hq, (next_c, next_cnt))
                heapq.heappush(hq, (cur_c, cur_cnt))

        return ''.join(ans)




# print(Solution().repeatLimitedString('cczazcc', 3))
print(Solution().repeatLimitedString('aababab', 2))