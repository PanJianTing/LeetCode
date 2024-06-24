from collections import deque

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            if nums[i] == 0 and i+k <= N:
                for j in range(i, i+k):
                    nums[j] = 0 if nums[j] else 1
                res += 1
        
        return res if len(set(nums)) == 1 else -1
    
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        N = len(nums)
        flipped = [False] * N
        pastFlipCnt = 0
        res = 0

        for i in range(N):
            if i >= k:
                if flipped[i-k]:
                    pastFlipCnt -= 1
            
            if (pastFlipCnt & 1) == nums[i]:
                if i+k > N:
                    return -1
                
                pastFlipCnt += 1
                flipped[i] = True
                res += 1
        
        return res
    
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        N = len(nums)
        q = deque()
        fliped = 0
        res = 0

        for i in range(N):
            if i >= k:
                fliped ^= q.popleft()
            
            if fliped == nums[i]:
                if i + k > N:
                    return -1
                q.append(1)
                res += 1
                fliped ^= 1
            else:
                q.append(0)

        return res
    
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cur_flip = 0
        res = 0

        for i in range(N):
            if i >= k and nums[i-k] == 2:
                cur_flip -= 1

            if (cur_flip & 1) == nums[i]:
                if i+k > N:
                    return -1
                
                cur_flip += 1
                nums[i] = 2
                res += 1
        return res




    
print(Solution().minKBitFlips([0,1,0], 1))
print(Solution().minKBitFlips([1,1,0], 2))
print(Solution().minKBitFlips([0,0,0,1,0,1,1,0], 3))
