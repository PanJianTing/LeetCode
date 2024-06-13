class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        res = 0
        N = len(seats)
        seats.sort()
        students.sort()

        for i in range(N):
            res += abs(seats[i] - students[i])

        return res
    
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        N = len(seats)
        max_count = max(seats)
        max_count = max(max(students) , max_count)
        difference = [0] * max_count
        matched = 0
        res = 0

        for i in range(N):
            difference[seats[i]-1] += 1
            difference[students[i]-1] -= 1
        
        for i in range(max_count):
            res = res + abs(matched)
            matched = matched - difference[i]
        
        return res



print(Solution().minMovesToSeat([3,1,5], [2,7,4]))
print(Solution().minMovesToSeat([4,1,5,9], [1,3,2,6]))
print(Solution().minMovesToSeat([2,2,6,6], [1,3,2,6]))