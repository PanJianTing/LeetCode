class Solution:
    def minimumCost(self, m: int, n: int, horiCut: list[int], verCut: list[int]) -> int:
        res = 0
        horiCut.sort()
        verCut.sort()
        h_part = 1
        v_part = 1
    
        while verCut and horiCut:

            if verCut[-1] > horiCut[-1]:
                res += verCut[-1] * h_part
                n -= 1
                verCut.pop()
                v_part += 1
            else:
                res += horiCut[-1] * v_part
                m -= 1
                horiCut.pop()
                h_part += 1

        return res + sum(verCut) * h_part + sum(horiCut) * v_part
    

    def minimumCost(self, m: int, n: int, horiCut: list[int], verCut: list[int]) -> int:
        res = 0
        horiCut.sort()
        verCut.sort()
        sum_h = sum(horiCut)
        sum_v = sum(verCut)
    
        while verCut and horiCut:

            if verCut[-1] > horiCut[-1]:
                res += verCut[-1] + sum_h            
                sum_v -= verCut.pop()
            else:
                res += horiCut[-1] + sum_v
                sum_h -= horiCut.pop()

        return res + sum_h + sum_v
                    


print(Solution().minimumCost(3,2, [1,3], [5]))
print(Solution().minimumCost(2,2, [7], [4]))
print(Solution().minimumCost(6,3, [2,3,2,3,1], [1,2]))
                


