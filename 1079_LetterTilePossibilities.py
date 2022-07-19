class Solution:
    '''
    用backtract
    例如：AAB

    1   2   3
        A - B
    A --  
        B - A
---------------------
        A - A
    B --

    '''

    def dfs(self, freq: dict) -> int:

        ans = 0

        if (freq.values()) == 0:
            return ans
        for tile in freq.keys():
            if freq[tile] == 0:
                continue
            
            freq[tile] -= 1
            ans += self.dfs(freq) + 1
            freq[tile] += 1     #因為可以重複，故要加回來。
        
        return ans

    def numTilePossibilities(self, tiles: str) -> int:

        char_freq = {}

        for char in tiles:
            count = char_freq.get(char, 0)
            char_freq[char] = count + 1
        return self.dfs(char_freq)

print(Solution().numTilePossibilities("AB"))
