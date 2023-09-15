from collections import defaultdict
import heapq

class Solution:
    def minDeletions(self, s):

        charMap = defaultdict(int)

        for c in s:
            charMap[c] += 1
        
        charList = list([-value for value in charMap.values()])
        heapq.heapify(charList)
        ans = 0

        while charList:
            cur = heapq.heappop(charList)
            if len(charList) == 0:
                break
            top = charList[0]

            if cur == top:
                ans += 1
                if (cur + 1) < 0:
                    heapq.heappush(charList, cur + 1)

        return ans
    
    def minDeletionss(self, s):
        charMap = defaultdict(int)
        charList = []

        for c in s:
            charMap[c] += 1
        
        for _, val in charMap.items():
            charList.append(val)

        ans = 0
        seen = set()

        for cnt in charList:
            if cnt in seen:
                while cnt > 0 and cnt in seen:
                    cnt -= 1
                    ans += 1
            seen.add(cnt)
        return ans
    
    def minDeletionss(self, s):
        charCnts = [0] * 26
        ans = 0

        for c in s:
            charCnts[ord(c) - ord('a')] += 1
        
        charCnts = [-cnt for cnt in charCnts if cnt > 0]
        
        heapq.heapify(charCnts)

        while len(charCnts) > 1:
            curr = heapq.heappop(charCnts)
            if  charCnts[0] == curr:
                curr += 1
                ans += 1
                if curr != 0:
                    heapq.heappush(charCnts, curr)
        return ans
                

print(Solution().minDeletions("aab"))
print(Solution().minDeletions("aaabbbcc"))
print(Solution().minDeletions("ceabaacb"))
print(Solution().minDeletions("bbcebab"))

        

