class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        
        result = []

        for _ in range(0, length):
            result.append(0)

        for update in updates:
            start = update[0]
            end = update[1]
            add = update[2]

            for index in range(start, end+1):
                result[index] += add
                

        # print(result)
        return result

class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:

        result = [0] * (length)

        for (start, end, add) in updates:
            result[start] += add
            if end + 1 < length:
                result[end +1] -= add

        before = 0

        for index in range(0, length):
            result[index] += before
            before = result[index]
        
        print(result)
        return result




Solution().getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]])
Solution().getModifiedArray(10, [[2,4,6],[5,6,8],[1,9,-4]])

