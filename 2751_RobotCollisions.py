class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        pairs = []
        N = len(positions)
        for i in range(N):
            pairs.append((positions[i], healths[i], directions[i], i))
        pairs.sort()

        st = []
        res = []

        for i in range(N):
            cur_p, cur_h, cur_d, cur_idx = pairs[i]
            while st:
                pre_p, pre_h, pre_d, pre_idx = st.pop()

                if pre_d == "R" and cur_d == "L":
                    if pre_h < cur_h:
                        cur_h -= 1
                    elif pre_h > cur_h:
                        cur_h = 0
                        st.append((pre_p, pre_h-1, pre_d, pre_idx))
                        break
                    else:
                        cur_h = 0
                        break
                else:
                    st.append((pre_p, pre_h, pre_d, pre_idx))
                    break
            if cur_h > 0:
                st.append((cur_p, cur_h, cur_d, cur_idx))


        st.sort(key=lambda pair: pair[3])
        for p, h, d, idx in st:
            res.append(h)
        return res
    

    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        N = len(positions)
        idxs = list(range(N))
        idxs.sort(key= lambda x: positions[x])
        st = []
        res = []

        for idx in idxs:
            if directions[idx] == "R":
                st.append(idx)
            else:
                while st and healths[idx] > 0:
                    cur_idx = st.pop()
                    if healths[cur_idx] > healths[idx]:
                        healths[cur_idx] -= 1
                        healths[idx] = 0
                        st.append(cur_idx)
                    elif healths[cur_idx] < healths[idx]:
                        healths[cur_idx] = 0
                        healths[idx] -= 1
                    else:
                        healths[cur_idx] = 0
                        healths[idx] = 0
        
        for h in healths:
            if h > 0:
                res.append(h)
        return res


print(Solution().survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR")) # [2, 17, 9, 15, 10]
print(Solution().survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL")) # [14]
print(Solution().survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL")) # []
print(Solution().survivedRobotsHealths([11,44,16], [1,20,17], "RLR")) # [18]
print(Solution().survivedRobotsHealths([1,40], [10,11], "RL")) # [10]
print(Solution().survivedRobotsHealths([3,40], [49,11], "LL")) # [49, 11]
            
            
                    
