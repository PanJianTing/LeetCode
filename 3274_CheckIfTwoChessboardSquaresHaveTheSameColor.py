from collections import defaultdict, deque
import heapq

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        black_odd = ['a', 'c', 'e', 'g']


        def check(cur):
            if cur[0] in black_odd:
                if int(cur[1]) & 1:
                    return 'b'
                else:
                    return 'w'
            else:
                if int(cur[1]) & 1:
                    return 'w'
                else:
                    return 'b'
        return check(coordinate1) == check(coordinate2)
    

    def checkTwoChessboards(self, cor1: str, cor2: str) -> bool:
        c1 = ord(cor1[0]) - ord('a')
        d1 = int(cor1[1]) - 1
        c2 = ord(cor2[0]) - ord('a')
        d2 = int(cor2[1]) - 1

        return (c1 + d1) & 1 == (c2 + d2) & 1