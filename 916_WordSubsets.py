

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        ans = []
        check_list = [0] * 26
        
        for w in words2:
            cur_list = [0] * 26
            for c in w:
                cur_list[ord(c) - ord('a')] += 1
            
            for i in range(26):
                check_list[i] = max(check_list[i], cur_list[i])
        
        for w in words1:
            is_subset = True
            cur_list = [0] * 26
            for c in w:
                cur_list[ord(c) - ord('a')] += 1
            
            for i in range(26):
                if check_list[i] != 0 and check_list[i] > cur_list[i]:
                    is_subset = False
                    break
            if is_subset:
                ans.append(w)
        
        return ans
    

    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        ans = set(words1)
        check_map = {}
        
        for w in words2:
            for c in w:
                cnt = w.count(c)
                if c not in check_map or cnt > check_map[c]:
                    check_map[c] = cnt
        
        for w in words1:
            for check_char in check_map:
                cnt = w.count(check_char)
                if check_map[check_char] > cnt:
                    ans.remove(w)
                    break
        
        return list(ans)
    

    

print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))