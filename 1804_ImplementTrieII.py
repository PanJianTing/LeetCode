from collections import defaultdict

class Trie:

    def __init__(self):
        self.cnt_map = defaultdict(int)
        
    def insert(self, word: str) -> None:
        self.cnt_map[word] += 1

    def countWordsEqualTo(self, word: str) -> int:
        return self.cnt_map[word]

    def countWordsStartingWith(self, prefix: str) -> int:
        N = len(prefix)
        res = 0
        for k in self.cnt_map.keys():
            if prefix == k[:N]:
                res += self.cnt_map[k]
        return res

    def erase(self, word: str) -> None:
        self.cnt_map[word] -= 1
        if self.cnt_map[word] == 0:
            del self.cnt_map[word]


class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.word_start_here = 0
        self.word_ending_here = 0

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')

            if node.links[idx] == None:
                node.links[idx] = TrieNode()
            node = node.links[idx]
            node.word_start_here += 1
        node.word_ending_here += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')

            if node.links[idx] == None:
                return 0
            node = node.links[idx]
        return node.word_ending_here

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')

            if node.links[idx] == None:
                return 0
            node = node.links[idx]
        return node.word_start_here

    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            node = node.links[idx]
            node.word_start_here -= 1
        node.word_ending_here -= 1
        
