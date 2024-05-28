from collections import defaultdict

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        N = len(s)
        M = len(pattern)
        pattern_map = defaultdict(str)
        word_set = set()

        def isMatch(pIdx, sIdx):
            if pIdx == M:
                return sIdx == N
            cur_p = pattern[pIdx]
            
            if cur_p in pattern_map:
                match_str = pattern_map[cur_p]
                need_str = s[sIdx:sIdx+len(match_str)]
                if match_str != need_str:
                    return False
                return isMatch(pIdx + 1, sIdx + len(match_str))
            else:
                for i in range(sIdx, N):
                    match_str = s[sIdx: i+1]
                    if match_str in word_set:
                        continue
                    pattern_map[cur_p] = match_str
                    word_set.add(match_str)
                    if isMatch(pIdx+1, i+1):
                        return True
                    del pattern_map[cur_p]
                    word_set.remove(match_str)
                
            return False
        
        return isMatch(0, 0)
        
print(Solution().wordPatternMatch("d", "e"))
print(Solution().wordPatternMatch("aaaa", "asdasdasdasd"))
print(Solution().wordPatternMatch("abab", "redblueredblue"))
print(Solution().wordPatternMatch("aabb", "xyzabcxzyabc"))
print(Solution().wordPatternMatch("ab", "aa"))


        