from collections import defaultdict
import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        N = len(hand)
        cnt_map = defaultdict(int)
        all_cnt = 0

        if N % groupSize:
            return False

        for n in hand:
            cnt_map[n] += 1
        
        all_cnt = len(cnt_map.keys())

        while all_cnt > 0:
            st = min(cnt_map.keys())

            for n in range(st, st+groupSize):
                
                if cnt_map[n] == 0:
                    return False
                cnt_map[n] -= 1
                if cnt_map[n] == 0:
                    all_cnt -= 1
                    del cnt_map[n]
        return True
    

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        N = len(hand)

        if N % groupSize:
            return False
        
        cnt_map = defaultdict(int)

        for n in hand:
            cnt_map[n] += 1
        
        hq = list(cnt_map.keys())
        heapq.heapify(hq)

        while hq:
            cur = hq[0]

            for i in range(cur, cur+groupSize):
                if cnt_map[i] == 0:
                    return False
                cnt_map[i] -= 1

                if cnt_map[i] == 0:
                    if i != heapq.heappop(hq):
                        return False
        return True
        

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        N = len(hand)
        
        if N % groupSize:
            return False
        
        cnt_map = defaultdict(int)

        for n in hand:
            cnt_map[n] += 1
        
        for n in hand:
            if cnt_map[n] == 0:
                continue
            st = n
            
            while cnt_map[st-1]:
                st -= 1
            
            for i in range(st, st+groupSize):
                cnt_map[i] -= 1
                if cnt_map[i] < 0:
                    return False
        return True
    
print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(Solution().isNStraightHand([1,2,3,6,2,2,4,7,8], 3))
print(Solution().isNStraightHand([1,2,3,4,5], 4))
print(Solution().isNStraightHand([8,10,12], 3))
print(Solution().isNStraightHand([8,8,9,7,7,7,6,7,10,6], 2))