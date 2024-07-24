class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        after_mapping = []
        res = []

        for i, n in enumerate(nums):
            if n == 0:
                after_mapping.append((mapping[0], i))
                continue
            mapping_num = 0
            cur_mul = 1
            while n > 0:
                mapping_num += (mapping[(n % 10)] * cur_mul)
                n //= 10
                cur_mul *= 10
            after_mapping.append((mapping_num, i))

        after_mapping.sort()

        for _, idx in after_mapping:
            res.append(nums[idx])
    
        return res
    
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        mapping_list = []
        res = []

        for i, n in enumerate(nums):
            mapping_nums = []
            nums_str = str(n)

            for c in nums_str:
                mapping_nums.append(str(mapping[int(c)]))
            
            mapping_list.append((int(''.join(mapping_nums)), i))
        
        mapping_list.sort()

        for _, idx in mapping_list:
            res.append(nums[idx])

        return res

print(Solution().sortJumbled([9,8,7,6,5,4,3,2,1,0], [0,1,2,3,4,5,6,7,8,9]))
print(Solution().sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))
print(Solution().sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]))
