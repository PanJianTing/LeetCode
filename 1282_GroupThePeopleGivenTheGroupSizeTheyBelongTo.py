from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSize):
        sizeMap = defaultdict(list)
        ans = []

        for i, size in enumerate(groupSize):
            sizeMap[size].append(i)
        
        for key in sizeMap.keys():
            if key == len(sizeMap[key]):
                ans.append(sizeMap[key])
            else:
                for i in range(0, len(sizeMap[key]), key):
                    ans.append(sizeMap[key][i: i+key])

        return ans
    
    def groupThePeople(self, groupSize):
        sizeMap = defaultdict(list)
        ans = []

        for i, size in enumerate(groupSize):
            sizeMap[size].append(i)
            if len(sizeMap[size]) == size:
                ans.append(sizeMap[size])
                sizeMap[size] = []
        return ans


print(Solution().groupThePeople([3,3,3,3,3,1,3]))
print(Solution().groupThePeople([1,1,1,2,2]))
