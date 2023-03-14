
from collections import defaultdict
import bisect

class Solution:

    def isSub(self, toCheck: str, inStr: str) -> bool:
        i = j = 0
        while i < len(toCheck) and j < len(inStr):
            if toCheck[i] == inStr[j]:
                i += 1
            j += 1

        return i == len(toCheck)

    def shortestWay(self, source: str, target: str) -> int:

        sourceSet = set(source)
        
        for c in target:
            if c not in sourceSet:
                return -1
            
        concatenated_source = source
        count = 1
        while self.isSub(target, concatenated_source) == False:
            concatenated_source += source
            count += 1
        return count
    
class Solution:
    def shortestWay(self, source: str, target: str) -> bool:

        sourceSet = set(source)

        for t in target:
            if t not in sourceSet:
                return -1
            
        m = len(source)

        i = 0

        count = 0

        for char in target:

            if i == 0:
                count += 1

            while source[i] != char:

                i = (i + 1) % m

                if i == 0:
                    count += 1
            
            i = (i + 1) % m

        return count
    

class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        char_to_indices = defaultdict(list)

        for i, c in enumerate(source):
            char_to_indices[c].append(i)


        source_iterator = 0
        count = 1

        for char in target:

            if char not in char_to_indices:
                return -1
            
            index = bisect.bisect_left(char_to_indices[char], source_iterator)

            if index == len(char_to_indices[char]):
                count += 1
                source_iterator = char_to_indices[char][0] + 1
            else:
                source_iterator = char_to_indices[char][index] + 1

        return count

print(Solution().shortestWay("abc", "abcbc"))
        