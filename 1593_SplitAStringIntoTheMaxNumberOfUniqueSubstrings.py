class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        seen = set()

        def split(cur_idx):

            if cur_idx == N:
                return 0
            max_l = 0
            for idx in range(cur_idx, N):
                cur_str = s[cur_idx: idx+1]
                if cur_str not in seen:
                    seen.add(cur_str)
                    max_l = max(max_l, 1+split(idx+1))
                    seen.remove(cur_str)
            
            return max_l
        
        return split(0)
    
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        seen = set()
        max_count = [0]

        def split(cur_idx, count, max_count):
            if max_count[0] > count + (N - cur_idx):
                return
            if cur_idx == N:
                max_count[0] = max(max_count[0], count)
                return
            for idx in range(cur_idx, N):
                cur_str = s[cur_idx: idx+1]
                if cur_str not in seen:
                    seen.add(cur_str)
                    split(idx+1, 1 + count, max_count)
                    seen.remove(cur_str)
        
        split(0, 0, max_count)
        return max_count[0]

    
print(Solution().maxUniqueSplit("ababccc"))


            

            
