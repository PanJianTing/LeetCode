class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:

        m = len(mat1)
        n = len(mat1[0])
        l = len(mat2[0])

        ans = []

        for i in range(m):
            res = []
            for j in range(l):
                sum = 0
                for k in range(n):
                    sum += mat1[i][k] * mat2[k][j]
                res.append(sum)

            ans.append(res)

        return ans
    
print(Solution().multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]))
# print(Solution().multiply([[1,-5]], [[12],[-1]]))
