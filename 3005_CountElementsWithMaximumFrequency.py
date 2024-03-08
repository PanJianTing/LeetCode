from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        max_freq = 0
        max_freq_cnt = 0

        for n in nums:
            cnt[n] += 1

        max_freq = max(cnt.values())

        for val in cnt.values():
            if max_freq == val:
                max_freq_cnt += val

        return max_freq_cnt
    
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freqs = [0] * 100
        max_freq = 0
        max_freq_count = 0
        for n in nums:
            freqs[n-1] += 1
        
        freqs.sort()
        max_freq = freqs[99]

        for i in range(99, -1, -1):
            if max_freq == freqs[i]:
                max_freq_count += max_freq
            else:
                break
        return max_freq_count
    
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq_cnt = defaultdict(int)
        max_freq = 0
        max_freq_cnt = 0

        for n in nums:
            freq_cnt[n] += 1
            if freq_cnt[n] > max_freq:
                max_freq = freq_cnt[n]
                max_freq_cnt = max_freq
            elif freq_cnt[n] == max_freq:
                max_freq_cnt += max_freq
        return max_freq_cnt