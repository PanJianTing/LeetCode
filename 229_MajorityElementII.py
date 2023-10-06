from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        N = len(nums)
        limitation = N // 3
        cnt_map = defaultdict(int)
        ans = []

        for n in nums:
            cnt_map[n] += 1
        
        for k, cnt in cnt_map.items():
            if cnt > limitation:
                ans.append(k)
        
        return ans
    
    def majorityElement(self, nums):
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None

        for n in nums:
            if candidate1 != None and candidate1 == n:
                count1 += 1
            elif candidate2 != None and candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        
        res = []
        count1 = 0
        count2 = 0
        

        for n in nums:
            if candidate1 != None and n == candidate1:
                count1 += 1
            elif candidate2 != None and n == candidate2:
                count2 += 1

        n = len(nums)
        if count1 > (n // 3):
            res.append(candidate1)
        if count2 > (n // 3):
            res.append(candidate2)
        
        return res
        
        

    
# print(Solution().majorityElement([1]))
# print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([4,2,1,1]))
# print(Solution().majorityElement([1,2]))