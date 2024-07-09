from collections import defaultdict
from collections import deque

class Solution:
    def findTheWinner(self, N: int, k: int) -> int:
        all_list = [i for i in range(1, N+1)]
        remove_set = set()
        idx = 0
        count = 0

        while len(remove_set) < N-1:
            if all_list[idx] not in remove_set: 
                count += 1
                if count == k:
                    remove_set.add(all_list[idx])
                    count = 0
            idx = ((idx+1) % N)
                

        return list(set(all_list) - remove_set)[0]

    def findTheWinner(self, N: int, k: int) -> int:
        all_list = [i for i in range(1, N+1)]
        cur = 0

        while len(all_list) > 1:
            remove_idx = (cur + k - 1) % len(all_list)
            all_list.pop(remove_idx)
            cur = remove_idx
        
        return all_list[0]
    
    def findTheWinner(self, N: int, k: int) -> int:
        q = deque()
        
        for i in range(1, N+1):
            q.append(i)

        while len(q) > 1:
            for _ in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q.popleft()
    
    def findTheWinner(self, N: int, k: int) -> int:

        def help(cur_n):
            if cur_n == 1:
                return 0
            return (help(cur_n-1) + k) % cur_n
        return help(N) + 1
    
    def findTheWinner(self, N: int, k: int) -> int:
        ans = 0
        for i in range(2, N+1):
            ans = (ans + k) % i
        return ans + 1
    
print(Solution().findTheWinner(5, 2))
print(Solution().findTheWinner(6, 5))