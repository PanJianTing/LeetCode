class Solution:
    # 都先加上，用isMax來決定要不要過濾掉
    def makeFancyString(self, s: str) -> str:

        result = ""
        before = ""
        isMax = False

        for c in s:
            if before == c:
                # 第三次以上
                if isMax == True:
                    continue
                else:
                    # 加第二次
                    isMax = True
            else:
                # 加第一次
                before = c
                isMax = False

            result += c
        return result

    def makeFancyString_my(self, s: str) -> str:
        
        result = ""
        beforeC = ""
        nowCCount = 0


        for c in s:
            if beforeC == c:
                nowCCount += 1
            else:
                nowCCount = 1
            
            if nowCCount < 3:
                result += c
            
            beforeC = c
        return result


Solution.makeFancyString(Solution(), "leeetcode")
