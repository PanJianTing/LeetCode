class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        splite = []

        wordCntList = []
        spaceChar = " "

        for w in words:
            wordCntList.append((len(w), w))
        
        temp = []
        currWidth = 0
        for cnt, w in wordCntList:
            
            if currWidth + cnt <= maxWidth:
                temp.append(w)
                currWidth += (cnt + 1)
            else:
                splite.append(temp)
                temp = [w]
                currWidth = cnt+1

        if temp:

            splite.append(temp)

        for i, temp in enumerate(splite):
            totalWidth = 0
            curCnt = 0
            
            for w in temp:
                curCnt += 1
                totalWidth += len(w)
            
            if curCnt == 1:
                ans.append(temp[0] + spaceChar * (maxWidth - totalWidth))
            elif i == len(splite) - 1:
                s = ""
                width = 0
                for w in temp:
                    if len(s) + len(w) < maxWidth:
                        s += w + spaceChar
                    else:
                        s += w
                
                ans.append(s + spaceChar * (maxWidth - len(s)))
            else:
                s = ""
                leaveWidth = maxWidth - totalWidth
                
                for i, w in enumerate(temp):
                    

                    if i == curCnt - 1:
                        s += w
                    else:
                        leaveCnt = curCnt - i - 1
                        spaceCnt = leaveWidth // leaveCnt
                        if leaveWidth % leaveCnt != 0:
                            spaceCnt += 1

                        if leaveWidth > spaceCnt:
                            s += w + (spaceChar * spaceCnt)
                            leaveWidth -= spaceCnt
                        else:
                            s += w + (spaceChar * leaveWidth)
                ans.append(s)

        return ans
    
# print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
# print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
# print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
print(Solution().fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))
                
                
