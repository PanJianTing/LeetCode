class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        st = []

        for c in s:
            if "#" == c:
                if ss:
                    ss.pop()
            else:
                ss.append(c)
        
        for c in t:
            if "#" == c:
                if st:
                    st.pop()
            else:
                st.append(c)

        return ss == st
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        skipS = 0
        skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if '#' == s[i]:
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if '#' == t[j]:
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        
        return True
    
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1
        skipS = 0
        skipT = 0

        while i >= 0 or j >= 0:

            while i >= 0:
                if "#" == s[i]:
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if "#" == t[j]:
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True


class Solution:
    def check(self, s: str) -> list:
        
        sAfter = []
        for char in s:
            if char == "#":
                sAfter = sAfter[:-1]
            else:
                sAfter.append(char)

        return sAfter

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)

    

    def backspaceCompare_my(self, s: str, t: str) -> bool:

        s = list(s)
        t = list(t)

        sAfter = []
        tAfter = []

        for char in s:
            if char == "#":
                sAfter = sAfter[:-1]
            else:
                sAfter.append(char)

        for char in t:
            if char == "#":
                tAfter = tAfter[:-1]
            else:
                tAfter.append(char)

        return sAfter == tAfter
    



    
print(Solution().backspaceCompare("bbbextm", "bbb#extm"))
# print(Solution().backspaceCompare("ab#c", "ad#c"))
# print(Solution().backspaceCompare("ab##", "c#d#"))
# print(Solution().backspaceCompare("a#c", "b"))
# print(Solution().backspaceCompare("a##c", "#a#c"))