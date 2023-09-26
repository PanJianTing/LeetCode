from collections import Counter, defaultdict

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
    

from collections import Counter, defaultdict

class Solution:
    def removeDuplicateLetters(self, s):

        N = len(s)
        char_dic = Counter(s)
        idx = 0

        for i in range(N):
            if s[i] < s[idx]:
                idx = i
            char_dic[s[i]] -= 1
            if char_dic[s[i]] == 0:
                break

        return "" if N == 0 else s[idx] + self.removeDuplicateLetters(s[idx:].replace(s[idx], ""))
    
    def removeDuplicateLetters(self, s):

        char_map = Counter(s)

        st = []

        seen = set()

        for c in s:

            if c not in seen:
                
                while st and c < st[-1] and char_map[st[-1]] > 0:
                    seen.remove(st.pop())
                
                
                st.append(c)
                seen.add(c)
            char_map[c] -= 1
        
        return "".join(st)
    
    def removeDuplicateLetters(self, s):

        last_idx_map = defaultdict(int)

        st = []

        seen = set()

        for i, c in enumerate(s):
            last_idx_map[c] = i

        for i, c in enumerate(s):

            if c not in seen:
                
                while st and c < st[-1] and last_idx_map[st[-1]] > i:
                    seen.remove(st.pop())

                st.append(c)
                seen.add(c)
        
        return "".join(st)



print(Solution().removeDuplicateLetters('bbcaac'))
print(Solution().removeDuplicateLetters('ecbacba'))
print(Solution().removeDuplicateLetters('bcabc'))
print(Solution().removeDuplicateLetters('cbacdcbc'))