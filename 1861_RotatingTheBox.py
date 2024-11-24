from collections import deque

class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        ROW = len(box)
        COL = len(box[0])
        ans = [[''] * ROW for _ in range(COL)] 

        for r in range(ROW):
            last_pos_q = deque()
            for c in range(COL-1, -1, -1):
                if box[r][c] == '.':
                    last_pos_q.append(c)
                elif box[r][c] == '*':
                    last_pos_q = deque()
                else:
                    if last_pos_q:
                        new_pos = last_pos_q.popleft()
                        box[r][new_pos] = '#'
                        box[r][c] = '.'
                        last_pos_q.append(c)

        for r in range(ROW):
            trans_c = ROW-1-r
            for c in range(COL):
                ans[c][trans_c] = box[r][c]
        
        return ans
    

    def rotateTheBox(self, box: list[list[int]]) -> list[list[int]]:
        ROW = len(box)
        COL = len(box[0])

        ans = [[''] * ROW for _ in range(COL)]

        for r in range(ROW):
            for c in range(COL):
                ans[c][r] = box[r][c]
        
        for c in range(COL):
            ans[c].reverse()

        for r in range(ROW):
            for c in range(COL-1, -1, -1):

                pos = -1

                if ans[c][r] == '.':
                    for k in range(c-1, -1, -1):
                        if ans[k][r] == '*':
                            break
                        elif ans[k][r] == '#':
                            pos = k
                            break
                
                if pos != -1:
                    ans[pos][r] = '.'
                    ans[c][r] = '#'
        return ans
    

    def rotateTheBox(self, box: list[list[int]]) -> list[list[int]]:
        ROW = len(box)
        COL = len(box[0])

        ans = [[''] * ROW for _ in range(COL)]

        for r in range(ROW):
            for c in range(COL):
                ans[c][r] = box[r][c]
        
        for c in range(COL):
            ans[c].reverse()

        ROW, COL = COL, ROW

        for c in range(COL):
            
            POS = ROW-1
            for r in range(ROW-1, -1, -1):
                if ans[r][c] == '#':
                    ans[r][c] = '.'
                    ans[POS][c] = '#'
                    POS -= 1
                elif ans[r][c] == '*':
                    POS = r-1

        return ans
        
        


print(Solution().rotateTheBox([["#",".","*","."], ["#","#","*","."]]))