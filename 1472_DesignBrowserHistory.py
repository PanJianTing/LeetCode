class Node:

    def __init__(self, url: str, next = None, forward= None) -> None:
        self.url = url
        self.next = next
        self.forward = forward


class BrowserHistory:

    now = None
    def __init__(self, homepage: str) -> None:
        self.now = Node(homepage)

    def visit(self, url: str) -> None:
        website = Node(url)
        self.now.next = website
        website.forward = self.now
        self.now = self.now.next
        return

    def back(self, steps: int) -> str:
        while self.now.forward and steps:
            self.now = self.now.forward
            steps -= 1

        return self.now.url

    def forward(self, steps: int) -> str:
        while self.now.next and steps:
            self.now = self.now.next
            steps -= 1

        return self.now.url
    
class BrowserHistory:

    def __init__(self, homepage: str) -> None:
        self.backList = []
        self.forwardList = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.backList.append(self.curr)
        self.curr = url
        self.forwardList = []

    def back(self, steps: int) -> str:
        while len(self.backList) and steps:
            self.forwardList.append(self.curr)
            self.curr = self.backList.pop()
            steps -= 1
        return self.curr
    
    def forward(self, steps: int) -> str:
        while len(self.forwardList) and steps:
            self.backList.append(self.curr)
            self.curr = self.forwardList.pop()
            steps -= 1
        return self.curr
    

class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited_url = [homepage]
        self.curr = 0
        self.last = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if len(self.visited_url) > self.curr:
            self.visited_url[self.curr] = url
        else:
            self.visited_url.append(url)

        self.last = self.curr
           

    def back(self, steps: int) -> str:
        if self.curr - steps < 0:
            self.curr = 0
        else:
            self.curr -= steps

        return self.visited_url[self.curr]
    
    def forward(self, steps: int) -> str:
        if self.curr + steps > self.last:
            self.curr = self.last
        else:
            self.curr += steps
        return self.visited_url[self.curr]
