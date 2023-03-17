from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.childNodes = {}
        self.isEnd = False

class Trie:

    root = TrieNode()
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.childNodes:
                node.childNodes[c] = TrieNode()
            node = node.childNodes[c]
        node.isEnd = True

    def searchPrefix(self, word: str) -> TrieNode:
        node = self.root
        for c in word:
            if c in node.childNodes:
                node = node.childNodes[c]
            else:
                return None
        
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node
    
class Trie:

    root = {}
    def __init__(self) -> None:
        self.root = {}

    def insert(self, word: str) -> None:

        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["*"] = ""

    def searchPrefix(self, word: str) -> dict:
        curr = self.root
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                return None
        
        return curr

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node and "*" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node
