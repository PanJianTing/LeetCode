import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hq = []
        res = ''
        if a > 0:
            heapq.heappush(hq, (-a, 'a'))
        
        if b > 0:
            heapq.heappush(hq, (-b, 'b'))
        
        if c > 0:
            heapq.heappush(hq, (-c, 'c'))

        while hq:
            cnt, cur_c = heapq.heappop(hq)
            cnt *= -1

            if len(res) > 1 and res[-1] == res[-2] and res[-2] == cur_c:
                if not hq:
                    break
                next_cnt, next_c = heapq.heappop(hq)
                next_cnt *= -1

                res += next_c
                next_cnt -= 1

                if next_cnt > 0:
                    heapq.heappush(hq, (next_cnt * -1, next_c))
            else:
                res += cur_c
                cnt -= 1
            
            if cnt > 0:
                heapq.heappush(hq, (cnt * -1, cur_c))


        return res

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        N = a + b + c
        cura = 0
        curb = 0
        curc = 0

        res = ''

        for _ in range(N):
            if (a >= b and a >= c and cura != 2) or (a > 0 and (curb == 2 or curc == 2)):
                res += 'a'
                a -= 1
                cura += 1
                curb = 0
                curc = 0
            elif (b >= a and b >= c and curb != 2) or (b > 0 and (cura == 2 or curc == 2)):
                res += 'b'
                b -= 1
                cura = 0
                curb += 1 
                curc = 0
            elif (c >= a and c >= b and curc != 2) or (c > 0 and (cura == 2 or curb == 2)):
                res += 'c'
                c -= 1
                cura = 0
                curb = 0
                curc += 1
            else:
                break
        
        return res
    
print(Solution().longestDiverseString(1, 1, 7))
print(Solution().longestDiverseString(7, 1, 0))
            


        