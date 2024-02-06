from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        N = len(strs)
        idx_map = defaultdict(list)
        ans = []

        for i in range(N):
            idx_map[str(sorted(strs[i]))].append(i)

        for _, idxs in idx_map.items():
            temp = []
            for idx in idxs:
                temp.append(strs[idx])
            ans.append(temp)
        return ans
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        N = len(strs)
        idx_map = defaultdict(list)
        ans = []

        for i in range(N):
            idx_map[tuple(sorted(strs[i]))].append(i)

        for _, idxs in idx_map.items():
            temp = []
            for idx in idxs:
                temp.append(strs[idx])
            ans.append(temp)
        return ans
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        N = len(strs)
        idx_map = defaultdict(list)

        for i in range(N):
            word = strs[i]
            idx_map[tuple(sorted(word))].append(word)

        return idx_map.values()
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        idx_map = defaultdict(list)

        for word in strs:
            idx_map[tuple(sorted(word))].append(word)

        return idx_map.values()
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        idx_map = defaultdict(list)

        for word in strs:
            temp = [0] * 26
            for c in word:
                temp[ord(c) - ord('a')] += 1
            idx_map[tuple(temp)].append(word)
        
        return idx_map.values()
        
        
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
        