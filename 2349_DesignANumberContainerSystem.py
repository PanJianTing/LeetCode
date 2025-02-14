from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):

        self.get_all_index_number = defaultdict(list)
        self.get_number_index = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.get_number_index:
            origin_number = self.get_number_index[index]
            origin_hq = self.get_all_index_number[origin_number]
            while len(origin_hq) > 0 and index == origin_hq[0]:
                heapq.heappop(origin_hq)
        
        self.get_number_index[index] = number
        hq = self.get_all_index_number[number]
        heapq.heappush(hq, index)

    def find(self, number: int) -> int:
        hq = self.get_all_index_number[number]
        if len(hq) == 0:
            return -1
        
        while hq:
            if self.get_number_index[hq[0]] == number:
                return hq[0]
            heapq.heappop(hq)
        
        return -1
    

class NumberContainers:

    def __init__(self):

        self.get_all_index_number = defaultdict(list)
        self.get_number_index = {}
        

    def change(self, index: int, number: int) -> None:
        
        self.get_number_index[index] = number
        hq = self.get_all_index_number[number]
        heapq.heappush(hq, index)

    def find(self, number: int) -> int:
        hq = self.get_all_index_number[number]
        if len(hq) == 0:
            return -1
        
        while hq:
            if self.get_number_index[hq[0]] == number:
                return hq[0]
            heapq.heappop(hq)
        
        return -1