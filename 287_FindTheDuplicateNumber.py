class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort()

        for i in range(1, N):
            if nums[i] == nums[i-1]:
                return nums[i]
                
        return nums[0]
    
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()

        for n in nums:
            if n in seen:
                return n
            seen.add(n)

        return nums[0]
    
    def findDuplicate(self, nums: list[int]) -> int:

        for n in nums:
            cur = abs(n)
            if nums[cur] < 0:
                return cur
            nums[cur] = nums[cur] * -1
        return -1
    
    def findDuplicate(self, nums: list[int]) -> int:

        def dp(cur):
            if nums[cur] == cur:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return dp(nxt)
        return dp(0)
    
    def findDuplicate(self, nums: list[int]) -> int:
        cur = 0
        while nums[cur] != cur:
            nxt = nums[cur]
            nums[cur] = cur
            cur = nxt
        return cur

    def findDuplicate(self, nums: list[int]) -> int:

        l = 0
        r = len(nums) - 1

        dup = -1

        while l <= r:
            cur = l + ((r - l) >> 1)

            cnt = 0
            for n in nums:
                if n <= cur:
                    cnt += 1
            
            if cnt > cur:
                dup = cur
                r = cur - 1
            else:
                l = cur + 1
        
        return dup
    
    
    def findDuplicate(self, nums):

        dup = 0
        N = len(nums) - 1
        bits = N.bit_length()

        for i in range(bits):
            mask = 1 << i
            base_cnt = 0
            nums_cnt = 0

            for j in range(0, N+1):
                if j & mask:
                    base_cnt += 1

                if nums[j] & mask:
                    nums_cnt += 1
            
            if nums_cnt - base_cnt > 0:
                dup |= mask

        return dup
    
    def findDuplicate(self, num):

        slow = num[0]
        fast = num[0]

        while True:
            slow = num[slow]
            fast = num[num[fast]]
            if slow == fast:
                break

        slow = num[0]
        while slow != fast:
            slow = num[slow]
            fast = num[fast]
        
        return slow




    

print(Solution().findDuplicate([1,3,4,2,2])) 
print(Solution().findDuplicate([3,1,3,4,2])) 
print(Solution().findDuplicate([2,5,9,6,9,3,8,9,7,1])) 