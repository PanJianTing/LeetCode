from collections import defaultdict

class Solution:
    def calcEquation(self, eqs: list[list[int]], values: list[float], qus: list[list[str]]) -> list[float]:

        # create adj list
        adjMap = defaultdict(list)
        seen = set()
        for i in range(len(eqs)):
            st, end = eqs[i]
            val = values[i]
            adjMap[st].append((end, val))
            adjMap[end].append((st, 1/val))

        def dfs(next: list[tuple], nowVal: float, target: str) -> float:

            for node, val in next:
                if node == target:
                    return nowVal * val
                elif node not in seen:
                    seen.add(node)
                    temp = dfs(adjMap[node], nowVal * val, target)
                    if temp != -1.0:
                        return temp

            return -1.0
        ans = []
        for q_st, q_end in qus:
            # print(q_st, q_end)
            seen = set()
            seen.add(q_st)
            if q_st not in adjMap or q_end not in adjMap:
                ans.append(-1.0)
            elif q_st == q_end:
                ans.append(1.0)
            else:
                ans.append(dfs(adjMap[q_st], 1.0, q_end))
        
        print(ans)
        return ans
    
Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
Solution().calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
Solution().calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]])