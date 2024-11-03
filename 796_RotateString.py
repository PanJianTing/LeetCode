class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        if len(goal) != N:
            return False

        for i in range(N):
            if s[i] == goal[0]:
                cur_idx = i
                is_match = True
                for j in range(N):
                    if s[cur_idx] != goal[j]:
                        is_match = False
                        break
                    cur_idx = (cur_idx + 1) % N
                if is_match:
                    return True
        return False
    

    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        if len(goal) != N:
            return False
        
        for _ in range(N):
            if s == goal:
                return True
            s = s[1:] + s[0]
        
        return False
    
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s

        return goal in s