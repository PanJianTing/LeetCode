class Solution:
    # MLE
    def decodeAtIndex(self, s, k) -> int:

        newS = []
        p = 0
        curStr = ""

        while len(newS) < k:
            if s[p].isdigit():
                for _ in range(int(s[p])):
                    newS.append(curStr)
            else:
                curStr += s[p]
            p += 1
            
        return newS[k-1]
    
    def decodeAtIndex(self, s, k) -> int:
        N = len(s)
        allL = 0
        for c in s:
            if c.isdigit():
                allL *= int(c)
            else:
                allL += 1

        for i in range(N-1, -1, -1):
            k %= allL
            if k == 0 and s[i].isdigit() == False:
                return s[i]
            
            if s[i].isdigit():
                allL /= int(s[i])
            else:
                allL -= 1
        
        return None
    
    def decodeAtIndex(self, s, k) -> int:
        N = 0

        for i, c in enumerate(s):
            if c.isdigit():
                N *= int(c)
            else:
                N += 1
            if k <= N:
                break
        for j in range(i, -1, -1):
            if s[j].isdigit():
                N /= int(s[j])
                k %= N
            else:
                if k == N or k == 0:
                    return s[j]
                N -= 1

    def decodeAtIndex(self, s, k) -> int:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(s):
            k %= size
            if k == 0 and c.isdigit() == False:
                return c
            
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
        
        return None


print(Solution().decodeAtIndex("a2b3c4d5e6f7g8h9", 10))
print(Solution().decodeAtIndex("leet2code3", 10))
print(Solution().decodeAtIndex("ha22", 5))
print(Solution().decodeAtIndex("a2345678999999999999999", 1))

