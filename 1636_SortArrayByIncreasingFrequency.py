from collections import defaultdict, Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        cnt_map = defaultdict(int)
        fre_map = defaultdict(list)
        res = []
        for n in nums:
            cnt_map[n] += 1
        
        for n, cnt in cnt_map.items():
            fre_map[cnt].append(n)
        
        for cnt in sorted(fre_map.keys()):
            ns = fre_map[cnt]
            ns.sort(reverse=True)
            for n in ns:
                res += [n] * cnt
        return res
    
    def frequencySort(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        nums.sort(key= lambda x: (counter[x], -x))
        return nums
        
print(Solution().frequencySort([1,1,2,2,2,3]))
print(Solution().frequencySort([2,3,1,3,2]))
print(Solution().frequencySort([-1,1,-6,4,5,-6,1,4,1]))