from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        be_trust_map = defaultdict(list)
        trust_map = defaultdict(list)

        for a, b in trust:
            be_trust_map[b].append(a)
            trust_map[a].append(b)
        
        for i in range(1, n+1):
            if len(be_trust_map[i]) == n-1 and len(trust_map[i]) == 0:
                return i
        return -1
    
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        be_trust_map = defaultdict(int)
        trust_map = defaultdict(int)

        for a, b in trust:
            be_trust_map[b] += 1
            trust_map[a] += 1
        
        for i in range(1, n+1):
            if be_trust_map[i] == n-1 and trust_map[i] == 0:
                return i
        
        return -1
    
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        be_trust_list = [0] * (n+1)
        trust_list = [0] * (n+1)

        for a, b in trust:
            be_trust_list[b] += 1
            trust_list[a] += 1
        
        for i in range(1, n+1):
            if be_trust_list[i] == n-1 and trust_list[i] == 0:
                return i
        return -1

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_score = [0] * (n+1)

        for a, b in trust:
            trust_score[b] += 1
            trust_score[a] -= 1
        
        for i in range(1, n+1):
            if trust_score[i] == n-1:
                return i
        return -1
            

print(Solution().findJudge(2, [[1,2]]))
print(Solution().findJudge(3, [[1,3],[2,3]]))
print(Solution().findJudge(3, [[1,3],[2,3],[3,1]]))