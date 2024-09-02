from collections import deque

class Solution:
    def pathSum(self, nums: list[int]) -> int:
        key_map = {}

        for n in nums:
            key_map[n//10] = n % 10
        
        def dfs(cur_node, cur_sum):
            
            d = cur_node // 10
            p = cur_node % 10

            next_left = (d+1) * 10 + (p << 1) - 1
            next_right = (d+1) * 10 + (p << 1)

            res = 0

            if next_left not in key_map and next_right not in key_map:
                return cur_sum
            
            if next_left in key_map:
                res += dfs(next_left, cur_sum + key_map[next_left])

            if next_right in key_map:
                res += dfs(next_right, cur_sum + key_map[next_right])
            return res
        
        return dfs(nums[0] // 10, nums[0] % 10)
    
    def pathSfum(self, nums: list[int]) -> int:
        key_map = {}
        ans = 0

        for n in nums:
            key_map[n // 10] = n % 10
        
        root = nums[0] // 10
        q = deque()
        q.append((root, nums[0] % 10))

        while q:
            cur_node, cur_sum = q.popleft()

            d = cur_node // 10
            p = cur_node % 10

            next_left = 10 * (d + 1) + (p << 1) - 1
            next_right = 10 * (d + 1) + (p << 1)
            
            if next_left not in key_map and next_right not in key_map:
                ans += cur_sum
                continue

            if next_left in key_map:
                q.append((next_left, cur_sum + key_map[next_left]))

            if next_right in key_map:
                q.append((next_right, cur_sum + key_map[next_right]))
        
        return ans
            
    
print(Solution().pathSum([113,215,221]))
print(Solution().pathSum([113,221]))