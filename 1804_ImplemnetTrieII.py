from collections import defaultdict

class Trie:

    def __init__(self) -> None:
        self.cnt_map = defaultdict(int)
    
    def insert(self, word: str) -> None:
        self.cnt_map[word] += 1
    
    def countWordsEqualTo(self, word: str) -> int:
        return self.cnt_map[word]
    
    def countWordsStartingWith(self, prefix: str) -> int:
        
        ans = 0
        for k, v in self.cnt_map.items():
            if k.startswith(prefix):
                ans += v
        
        return ans
    
    def erase(self, word: str) -> None:
        self.cnt_map[word] -= 1

        if self.cnt_map[word] <= 0:
            del self.cnt_map[word]

class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.start = 0
        self.end = 0

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.links[idx] == None:
                cur.links[idx] = TrieNode()
            cur = cur.links[idx]
            cur.start += 1
        cur.end += 1
    
    def countWordsEqualTo(self, word) -> int:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.links[idx] == None:
                return 0
            cur = cur.links[idx]
        return cur.end
    
    def countWordsStartingWith(self, word) -> int:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.links[idx] == None:
                return 0
            cur = cur.links[idx]
        return cur.start
    
    def erase(self, word):
        cur = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if cur.links[idx] == None:
                return
            cur = cur.links[idx]
            cur.start -= 1
        cur.end -= 1

                
    

