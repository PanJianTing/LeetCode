class Solution:
    def maxBoxesInWarehouse(self, boxes: list[int], warehouses: list[int]) -> int:
        N = len(warehouses)
        M = len(boxes)
        boxes.sort()
        effectHs = [0] * N
        min_h = float('inf')
        res = 0
        idx = 0
        
        for i in range(N):
            min_h = min(min_h, warehouses[i])
            effectHs[i] = min_h
        
        min_h = float('inf')
        for i in range(N-1, -1, -1):
            min_h = min(min_h, warehouses[i])
            effectHs[i] = max(effectHs[i], min_h)

        effectHs.sort()
        for i in range(N):
            if idx < M and boxes[idx] <= effectHs[i]:
                res += 1
                idx += 1
        return res
    

    def maxBoxesInWarehouse(self, boxes: list[int], warehouse:list[int]) -> int:
        M = len(boxes)
        N = len(warehouse)
        l = 0
        r = N-1
        idx = 0
        res = 0

        boxes.sort(reverse=True)

        while l <= r and idx < M:
            if boxes[idx] <= warehouse[l]:
                l += 1
                res += 1
            elif boxes[idx] <= warehouse[r]:
                r -= 1
                res += 1
            idx += 1
        return res
    

print(Solution().maxBoxesInWarehouse([1,2,2,3,4], [3,4,1,2]))
print(Solution().maxBoxesInWarehouse([3,5,5,2], [2,1,3,4,5]))