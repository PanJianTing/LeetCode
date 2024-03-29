from inspect import stack
from typing import Counter


# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:

#         # find pos - the index of the leftmost letter in our solution
#         # we create a counter and end the iteration once the suffix doesn't have each unique character
#         # pos will be the index of the smallest character we encounter before the iteration ends

#         c = Counter(s)
#         pos = 0
#         for i in range(len(s)):
#             if s[i] < s[pos]:
#                 pos = i
#             c[s[i]] -= 1
#             if c[s[i]] == 0:
#                 break
#         # our answer is the leftmost letter plus the recursive call on the remainder of the string
#         # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
#         return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

class Solution:
    def removeDuplicateLetters(self, s) -> int:

        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, char in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if char not in seen:
                # if the last letter in our solution:
                #   1. exists
                #   2. is greater than char so removing it will make string smaller
                #   3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())

                seen.add(char)
                stack.append(char)
        return ''.join(stack)



Solution().removeDuplicateLetters("cbacdcbc")