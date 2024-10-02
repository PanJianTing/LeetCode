from collections import defaultdict

class Node:
    def __init__(self, freq) -> None:
        self.freq = freq
        self.pre = None
        self.next = None
        self.keys = set()


class AllOne:
    
    def __init__(self) -> None:
        self.cnt_map = defaultdict(int)
        self.is_change = False
        self.cur_max_str = ''
        self.cur_min_str = ''

    def inc(self, key: str) -> None:
        self.cnt_map[key] += 1
        self.is_change = True
    
    def dec(self, key: str) -> None:
        self.cnt_map[key] -= 1
        if self.cnt_map[key] == 0:
            del self.cnt_map[key]
        self.is_change = True


    def getMaxKey(self) -> str:
        if self.is_change:
            self.change()
        return self.cur_max_str
    
    def getMinKey(self) -> str:
        if self.is_change:
            self.change()
        return self.cur_min_str
    

    def change(self):
        cur_max_cnt = 0
        cur_min_cnt = float('inf')
        self.cur_max_str = ''
        self.cur_min_str = ''

        for k in self.cnt_map.keys():
            cur_cnt = self.cnt_map[k]
            if cur_cnt > cur_max_cnt:
                self.cur_max_str = k
                cur_max_cnt = cur_cnt
            
            if cur_cnt < cur_min_cnt:
                self.cur_min_str = k
                cur_min_cnt = cur_cnt
        self.is_change = False



# class AllOne:

#     def __init__(self):





all_one = AllOne()
all_one.inc("hello")
all_one.inc("hello")
print(all_one.getMaxKey())
print(all_one.getMinKey())

all_one.dec("hello")
all_one.dec("hello")

print(all_one.getMinKey())
all_one.inc("hello")
print(all_one.getMaxKey())


