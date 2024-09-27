from collections import defaultdict
from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self) -> None:
        self.single = []
        self.double = []


    def book(self, cur_start: int, cur_end: int) -> bool:
        for st, end in self.double:
            if max(st, cur_start) < min(end, cur_end):
                 return False

        for st, end in self.single:
            if max(st, cur_start) < min(end, cur_end):
                self.double.append([max(st, cur_start), min(end, cur_end)])
        self.single.append([cur_start, cur_end])
        return True


class MyCalendarTwo:
    def __init__(self) -> None:
        self.count_map = defaultdict(int)
        self.limit_count = 2

    def book(self, start, end) -> bool:
        self.count_map[start] += 1
        self.count_map[end] -= 1

        cur_count = 0

        for k in sorted(self.count_map.keys()):
            cur_count += self.count_map[k]

            if cur_count > self.limit_count:
                self.count_map[start] -= 1
                self.count_map[end] += 1

                if self.count_map[start] == 0:
                    del self.count_map[start]
                
                if self.count_map[end] == 0:
                    del self.count_map[end]
                
                return False
        return True
    

class MyCalendarTwo:
    def __init__(self) -> None:
        self.count_map = SortedDict(int)
        self.limit_count = 2

    def book(self, start, end) -> bool:
        self.count_map[start] = self.count_map.get(start, 0) + 1
        self.count_map[end] = self.count_map.get(end, 0) - 1

        cur_count = 0

        for cnt in self.count_map.values():
            cur_count += cnt

            if cur_count > self.limit_count:
                self.count_map[start] -= 1
                self.count_map[end] += 1

                if self.count_map[start] == 0:
                    del self.count_map[start]
                
                if self.count_map[end] == 0:
                    del self.count_map[end]
                
                return False
        return True
    


    

# o = MyCalendarTwo()

# print(o.book(10, 20))
# print(o.book(50, 60))
# print(o.book(10, 40))
# print(o.book(5, 15))
# print(o.book(5, 10))
# print(o.book(25, 55))



o = MyCalendarTwo()

print(o.book(12,26))
print(o.book(70,85))
print(o.book(55,67))
print(o.book(2,13))
print(o.book(3,18))
print(o.book(91,100))
print(o.book(13,26))
print(o.book(17,27))
print(o.book(41,55))
print(o.book(15,26))
print(o.book(50,68))

print(o.book(34,52))
print(o.book(95,100))
print(o.book(23,33))
print(o.book(89,100))
print(o.book(27,43))
print(o.book(80,95))
print(o.book(97,100))
print(o.book(28,47))
print(o.book(45,58))
print(o.book(76,93))
print(o.book(56,75))
print(o.book(91,100))
print(o.book(61,77))
print(o.book(36,49))
print(o.book(18,32))
print(o.book(96,100))
print(o.book(96,100))
print(o.book(67,86))
print(o.book(46,64))
print(o.book(95,100))
print(o.book(17,35))
print(o.book(8,27))
print(o.book(4,14))
print(o.book(30,43))
print(o.book(74,89))
print(o.book(77,95))
print(o.book(98,100))
print(o.book(31,41))
print(o.book(35,53))
        

    