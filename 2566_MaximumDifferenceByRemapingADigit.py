class Solution:
    def minMaxDifference(self, num: int) -> int:
        digit_list = str(num)
        N = len(digit_list)
        max_num = num
        min_num = num

        for i in range(N):
            if digit_list[i] != '9':
                max_num = int(digit_list.replace(digit_list[i], '9'))
                break

        for i in range(N):
            if digit_list[i] != '0':
                min_num = int(digit_list.replace(digit_list[i], '0'))
                break


        return max_num - min_num