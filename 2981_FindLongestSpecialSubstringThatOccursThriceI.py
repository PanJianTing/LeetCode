from collections import defaultdict, deque

class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        ans = 0
        cnt_map = defaultdict(int)

        for size in range(1, N+1):
            temp_list = deque()
            for c in s:
                temp_list.append(c)
                if len(temp_list) == size:
                    cnt_map[''.join(temp_list)] += 1
                    temp_list.popleft()
                

        for k, v in cnt_map.items():
            if v >= 3 and len(set(k)) == 1:
                ans = max(ans, len(k))
        
        return -1 if ans == 0 else ans
    
    def maximumLength(self, s: str) -> int:
        N = len(s)
        ans = 0
        cnt_map = defaultdict(int)

        for st in range(N):
            cur_list = []
            for end in range(st, N):
                cur_c = s[end]
                if cur_list and cur_list[-1] != cur_c:
                    break
                cur_list.append(cur_c)
                cnt_map[''.join(cur_list)] += 1

        for k, v in cnt_map.items():
            if v >= 3:
                ans = max(ans, len(k)) 

        return -1 if ans == 0 else ans

    def maximumLength(self, s: str) -> int:
        N = len(s)
        cnt_map = defaultdict(int)
        ans = 0

        for st in range(N):
            cur_char = s[st]
            cur_length = 1
            cnt_map[(cur_char, cur_length)] += 1
            for end in range(st+1, N):
                if s[end] == cur_char:
                    cur_length += 1
                    cnt_map[(cur_char, cur_length)] += 1
                else:
                    break
        
        for (c, l), count in cnt_map.items():
            if count >= 3:
                ans = max(ans, l)

        return -1 if ans == 0 else ans
    


    def maximumLength(self, s: str) -> int:
        N = len(s)
        cnt_map = defaultdict(int)
        ans = 0

        for end in range(N):
            for st in range(0, end+1):
                cur_str = s[st: end+1]
                if cur_str and len(set(cur_str)) == 1:
                    cnt_map[cur_str] += 1
        
        for k, v in cnt_map.items():
            if v >= 3:
                ans = max(ans, len(k)) 

        return -1 if ans == 0 else ans

print(Solution().maximumLength('cccerrrecdcdccedecdc'))
print(Solution().maximumLength('aaaa'))
    
            

