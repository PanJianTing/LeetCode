from collections import defaultdict

class Solotion:
    def queryResults(self, limit: int, Q: list[list[int]]) -> list[int]:
        N = limit + 1
        color_cnt_map = defaultdict(int)
        color_map = defaultdict(int)
        ans = []

        for idx, color in Q:
            if idx in color_map:
                origin_color = color_map[idx]
                if origin_color in color_cnt_map:
                    color_cnt_map[origin_color] -= 1
                    if color_cnt_map[origin_color] == 0:
                        del color_cnt_map[origin_color]
                

            color_cnt_map[color] += 1
            color_map[idx] = color
            ans.append(len(color_cnt_map))

        return ans
    

print(Solotion().queryResults(1, [[0,4],[0,4],[1,4],[1,2],[1,1]]))
print(Solotion().queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))