from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        N = len(nums)
        nums = sorted(nums)
        ans = 0

        for aIdx in range(N):
            for bIdx in range(N-1, aIdx, -1):
                product = nums[aIdx] * nums[bIdx]
                
                for cIdx in range(aIdx+1, bIdx):
                    if product % nums[cIdx] == 0:
                        all_set = set(nums)
                        all_set.remove(nums[aIdx])
                        all_set.remove(nums[bIdx])
                        all_set.remove(nums[cIdx])
                        if (product // nums[cIdx]) in all_set:
                            ans += 4
        return ans

    def tupleSameProduct(self, nums: list[int]) -> int:
        N = len(nums)
        nums = sorted(nums)
        ans = 0

        for aIdx in range(N):
            for bIdx in range(N-1, aIdx, -1):
                product = nums[aIdx] * nums[bIdx]
                check_set = set()
                for cIdx in range(aIdx+1, bIdx):
                    if product % nums[cIdx] == 0:
                        check_num = product // nums[cIdx]

                        if check_num in check_set:
                            ans += 8
                    
                    check_set.add(nums[cIdx])
        return ans
    
    def tupleSameProduct(self, nums: list[int]) -> int:
        N = len(nums)
        product_map = defaultdict(int)
        ans = 0

        for idx1 in range(N):
            for idx2 in range(idx1+1, N):
                product_map[nums[idx1] * nums[idx2]] += 1
        
        for val in product_map.values():
            ans += (8 * (val * (val - 1))) >> 1

        return ans
    

    def tupleSameProduct(self, nums: list[int]) -> int:
        N = len(nums)
        product_map = {}
        ans = 0

        for idx1 in range(N):
            for idx2 in range(idx1+1, N):
                cur = nums[idx1] * nums[idx2]
                if cur in product_map:
                    ans += product_map[cur]
                    product_map[cur] += 1
                else:
                    product_map[cur] = 1
        return ans * 8


print(Solution().tupleSameProduct([2,3,4,6]))
print(Solution().tupleSameProduct([1,2,4,5,10]))
print(Solution().tupleSameProduct([2,3,4,6,8,12]))