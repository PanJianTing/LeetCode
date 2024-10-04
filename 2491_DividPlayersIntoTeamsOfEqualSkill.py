from collections import defaultdict

class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        N = len(skill)
        skill.sort()
        
        l = 1
        r = N-2
        check_sum = skill[0] + skill[-1]
        res = skill[0] * skill[-1]

        while l < r:
            cur_sum = skill[l] + skill[r]
            if cur_sum != check_sum:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res
    

    def dividePlayers(self, nums: list[int]) -> int:
        N = len(nums)
        sum_nums = sum(nums)

        if sum_nums % (N >> 1):
            return -1

        pair_sum = (sum_nums // (N >> 1))
        cnt_map = defaultdict(int)
        res = 0

        for n in nums:
            cnt_map[n] += 1
        
        for k in cnt_map.keys():
            pair_k = pair_sum - k
            if cnt_map[pair_k] == cnt_map[k]:
                if pair_k == k:
                    res += (k * pair_k * (cnt_map[k] >> 1))
                else:
                    res += (k * pair_k * cnt_map[k])
                cnt_map[pair_k] = 0
                cnt_map[k] = 0
            else:
                return -1

        return res
    

    def dividePlayers(self, nums: list[int]) -> int:
        N = len(nums)
        sum_nums = sum(nums)

        if sum_nums % (N >> 1):
            return -1

        pair_sum = (sum_nums // (N >> 1))
        cnt_map = defaultdict(int)
        res = 0

        for n in nums:
            cnt_map[n] += 1
        
        for n in nums:
            pair_n = pair_sum - n

            if cnt_map[pair_n] == 0:
                return -1
            
            res += n * pair_n
            cnt_map[pair_n] -= 1
        return res >> 1

print(Solution().dividePlayers([3,2,5,1,3,4])) 
print(Solution().dividePlayers([3,4])) 
print(Solution().dividePlayers([1,1,2,3])) 

        

