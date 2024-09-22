from collections import defaultdict

class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        N = len(message)
        count = 0

        for m in message:
            for b in bannedWords:

                if m == b:
                    count += 1
                    break

        return count >= 2
    

    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        ban_count = 0
        m_map = defaultdict(int)

        for m in message:
            m_map[m] += 1
        
        for b in set(bannedWords):
            if b in m_map:
                ban_count += m_map[b]
        
        return ban_count >= 2
    

    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        s = set(bannedWords)
        return sum(m in s for m in message) > 1
    
print(Solution().reportSpam(["hello","world","leetcode"], ["world","hello"]))
print(Solution().reportSpam(["hello","programming","fun"], ["world","programming","leetcode"]))
print(Solution().reportSpam(["o","k","r","y","w","r"], ["k","b","s","a","s","u"]))
print(Solution().reportSpam(["s","a","aj","ps","h","ou","e","i","x"], ["j","a","b","fa","z","a","no","ih","nq"]))