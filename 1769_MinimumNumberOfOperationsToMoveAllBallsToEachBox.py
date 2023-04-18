class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        res = []

        oneIndex = []
        
        for i, box in enumerate(boxes):
            if box == "1":
                oneIndex.append(i)

        for i in range(len(boxes)):
            step = 0
            for one in oneIndex:
                step += abs(one - i)
            res.append(step)

        return res
    
    def minOperations(self, boxes: str) -> list[int]:

        res = [0] * len(boxes)
        op = 0
        cnt = 0
        for i in range(len(boxes)):
            res[i] += op
            cnt += boxes[i] == '1'
            op += cnt
        op = 0
        cnt = 0
        for i in range(len(boxes)-1, -1, -1):
            res[i] += op
            cnt += boxes[i] == '1'
            op += cnt
        return res
    
Solution().minOperations("110")
Solution().minOperations("001011")
