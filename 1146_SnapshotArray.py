import bisect

class SnapshotArray:

    history = []
    snapIdx = 0

    def __init__(self, length: int) -> None:
        self.history = [[(0,0)] for _ in range(length)]
        self.snapIdx = 0
    
    def set(self, idx, val):
        self.history[idx].append((self.snapIdx, val))
    
    def snap(self) -> int:
        temp = self.snapIdx
        self.snapIdx += 1
        return temp
    
    def get(self, idx, snap_idx) -> int:
        historyId = bisect.bisect_right(self.history[idx], snap_idx, key=lambda a:a[0])
        return self.history[idx][historyId-1][1]

class SnapshotArray:

    A = []
    snapIdx = 0

    def __init__(self, length) -> None:
        self.A = [[[-1, 0]] for _ in range(length)]
        self.snapIdx = 0
    
    def set(self, idx, val):
        self.A[idx].append([self.snapIdx, val])

    def snap(self) -> int:
        self.snapIdx += 1
        return self.snapIdx - 1

    def get(self, idx, snap_id) -> int:
        i = bisect.bisect(self.A[idx], [snap_id+1])-1
        return self.A[idx][i][1]