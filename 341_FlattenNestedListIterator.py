class NestedIterator:

    def __init__(self, nestedList: ['NestedInteger']):
        self.res = []
        self.dp(nestedList)
        self.allCnt = len(self.res)
        self.now_idx = 0
    
    def dp(self, mList: ['NestedInteger']):
        N = len(mList)
        for i in range(N):
            if mList[i].isInteger():
                self.res.append(mList[i].getInteger())
            else:
                self.dp(mList[i].getList())

    def next(self) -> int:
        temp = self.res[self.now_idx]
        self.now_idx += 1
        return temp
    
    def hasNext(self) -> bool:
        if self.now_idx >= self.allCnt:
            return False
        return True
    

class NestedIterator:

    def __init__(self, nestedList: ['NestedInteger']) -> None:
        self.st = list(reversed(nestedList))
    
    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.st.pop().getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.st) > 0
        
    def make_stack_top_an_integer(self):
        while self.st and not self.st[-1].isInteger():
            self.st.extend(reversed(self.st.pop().getList()))
