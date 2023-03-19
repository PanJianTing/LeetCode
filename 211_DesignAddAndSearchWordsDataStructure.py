from collections import defaultdict

class WordDictionary:

    def __init__(self) -> None:
        self.wordMap = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.wordMap[len(word)].add(word)
    
    def search(self, word: str) -> bool:

        m = len(word)

        for w in self.wordMap[m]:
            i = 0
            while i < m and (word[i] == w[i] or word[i] == '.'):
                i += 1

            if i == m:
                return True
        return False






class CharNode:

    def __init__(self) -> None:
        self.wordMap = defaultdict(CharNode)
        self.isEnd = False

class WordDictionary:
    def __init__(self) -> None:
        self.head = CharNode()

    def addWord(self, word: str) -> None:

        curr = self.head

        for c in word:
            curr = curr.wordMap[c]

        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.head
        self.res = False
        self.dfs(curr, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isEnd:
                self.res = True
            return 
        
        if word[0] == '.':
            for n in node.wordMap.values():
                self.dfs(n, word[1:])
        else:
            node = node.wordMap[word[0]]
            if not node:
                return
            self.dfs(node, word[1:])


class WordDictionary:

    node = {}

    def __init__(self) -> None:
        self.node = {}

    def addWord(self, word: str) -> None:

        curr = self.node

        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        curr['$'] = True

        return

    def search(self, word: str) -> bool:

        curr = self.node

        def searchInNode(word, node):

            for i, c in enumerate(word):
                if c in node:
                    node = node[c]
                else:
                    if c == '.':
                        for key in node:
                            if key not in '$' and searchInNode(word[i+1:], node[key]):
                                return True
                    return False
            return '$' in node
            

        return searchInNode(word, curr)