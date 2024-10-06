from collections import deque

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        d1 = deque(s1.split())
        d2 = deque(s2.split())

        while d1 and d2 and d1[0] == d2[0]:
            d1.popleft()
            d2.popleft()
        
        while d1 and d2 and d1[-1] == d2[-1]:
            d1.pop()
            d2.pop()

        return len(d1) == 0 or len(d2) == 0
    

    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1_list = s1.split()
        s2_list = s2.split()

        M = len(s1_list)
        N = len(s2_list)

        if M > N:
            return self.areSentencesSimilar(s2, s1)

        st = 0
        end1 = M-1
        end2 = N-1

        while st < M and s1_list[st] == s2_list[st]:
            st += 1
        
        while end1 > -1 and s1_list[end1] == s2_list[end2]:
            end1 -= 1
            end2 -= 1
        return end1 < st

print(Solution().areSentencesSimilar("My name is Haley", "My Haley"))




