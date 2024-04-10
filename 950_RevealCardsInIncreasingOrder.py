from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        N = len(deck)
        res = [0] * N
        deck.sort()
        cur_idx = 0
        res_idx = 0
        fill = True

        while cur_idx < N:
            if res[res_idx] == 0:
                if fill:
                    res[res_idx] = deck[cur_idx]
                    cur_idx += 1
                fill = not fill
            res_idx = (res_idx + 1) % N
        return res
    
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        N = len(deck)
        res = [0] * N
        deck.sort()
        q = deque()
        fill = True
        deck_idx = 0

        for i in range(N):
            q.append(i)

        while q:
            if fill:
                cur_idx = q.popleft()
                res[cur_idx] = deck[deck_idx]
                deck_idx += 1
            else:
                q.append(q.popleft())
            fill = not fill
        return res
    
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        N = len(deck)
        res = [0] * N
        deck.sort()
        q = deque()

        for i in range(N):
            q.append(i)

        for card in deck:
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())
        return res
print(Solution().deckRevealedIncreasing([17,13,11,2,3,5,7]))
