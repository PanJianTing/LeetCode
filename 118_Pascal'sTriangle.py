class Solution:
    def generate(self, r):
        if r == 1:
            return [[1]]
        
        triangle = [[1]]
        cur = 1
        while cur < r:
            temp = []
            for i in range(cur+1):
                if 0 < i < (cur):
                    temp.append(triangle[cur-1][i-1] + triangle[cur-1][i])
                else:
                    temp.append(1)
            triangle.append(temp)
            cur += 1
        return triangle
    
    def generate(self, r):
        if r == 1:
            return [[1]]

        be = self.generate(r-1)
        temp = []
        for i in range(r):
            if 0 < i < r-1:
                temp.append(be[r-2][i-1] + be[r-2][i])
            else:
                temp.append(1)
        be.append(temp)
        return be
    
    def generate(self, r):
        triangle = [[1]]
        
        for i in range(1, r):
            before = triangle[i-1]
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(before[j-1] + before[j])
            temp.append(1)
            triangle.append(temp)
        return triangle
    

print(Solution().generate(5))

            