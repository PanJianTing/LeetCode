
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mapping = {}
        for i , num in enumerate(nums):
            print(i , num)
            if num in mapping and abs(mapping[num] - num) <= k:
                return True
            else:
                mapping[num] = i
        return False
        
    
    def containsNearbyDuplicate_my(self, nums: list[int], k: int) -> bool:
        duplicateMap = {}
        
        for i in range(len(nums)):
            if nums[i] in duplicateMap:
                duplicateMap[nums[i]].append(i)
            else:
                duplicateMap[nums[i]] = [i]
                
        for key in duplicateMap.keys():
            indexList = duplicateMap[key]
            if len(indexList) > 1:
                print(indexList)
                for i in range(len(indexList)-1, 0, -1):
                    # print(indexList[i])
                    if abs(indexList[i] - indexList[i-1]) <= k:
                        return True
        return False

print(Solution.containsNearbyDuplicate(Solution(), [1,2,3,1], 3))
print(Solution.containsNearbyDuplicate(Solution(), [1,0,1,1], 1))
print("Hello World!")