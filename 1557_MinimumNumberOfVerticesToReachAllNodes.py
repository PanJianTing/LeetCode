class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:

        havePath = [True] * n
        ans = set()

        for edge in edges:
            havePath[edge[1]] = False
        
        for node in range(0, n):
            if havePath[node]:
                ans.add(node)
        
        return ans  

# print(Solution().findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))
# print(Solution().findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))


print(Solution().findSmallestSetOfVertices(5, [[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]))
