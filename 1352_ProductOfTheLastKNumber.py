class ProductOfNumbers:
    def __init__(self):
        self.prefix_list = [1]
        

    def add(self, num: int) -> None:
        if self.prefix_list[-1] == 0:
            self.prefix_list.append(num)
            return 
        self.prefix_list.append(self.prefix_list[-1] * num)
        if num == 0:
            N = len(self.prefix_list)
            self.prefix_list = [0] * (N-1)
            self.prefix_list.append(1)
        

    def getProduct(self, k: int) -> int:
        N = len(self.prefix_list)
        idx = N - k - 1 
        if idx < 0 or self.prefix_list[idx] == 0:
            return 0
        return self.prefix_list[-1] // self.prefix_list[idx]
    


pn = ProductOfNumbers()
pn.add(3)
pn.add(0)
pn.add(2)
pn.add(5)
pn.add(4)
print(pn.getProduct(2))
print(pn.getProduct(3))
print(pn.getProduct(4))
pn.add(8)
print(pn.getProduct(2))



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)