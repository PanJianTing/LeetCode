class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        N = len(sandwiches)
        cur_sd = 0

        while cur_sd < N and (sandwiches[cur_sd] in students):
            cur_st = students.pop(0)
            if cur_st == sandwiches[cur_sd]:
                cur_sd += 1
            else:
                students.append(cur_st)
        return N - cur_sd
    
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        
        while sandwiches and (sandwiches[0] in students):
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students.pop(0))
        return len(students)
    
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        zero_cnt = 0
        ones_cnt = 0

        for st in students:
            if st == 0:
                zero_cnt += 1
            else:
                ones_cnt += 1
        
        for sd in sandwiches:
            if sd == 0 and zero_cnt == 0:
                return ones_cnt

            if sd == 1 and ones_cnt == 0:
                return zero_cnt

            if sd == 0:
                zero_cnt -= 1
            else:
                ones_cnt -= 1
        return 0

    
print(Solution().countStudents([1,1,0,0], [0,1,0,1]))
print(Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))