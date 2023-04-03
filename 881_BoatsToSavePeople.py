class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(reverse=True)
        
        ans = 0
        left = 0
        right = len(people) - 1

        while left <= right:

            if people[left] + people[right] <= limit:
                ans += 1
                right -= 1
            elif people[left] <= limit:
                ans += 1

            left += 1

        return ans
    
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        ans = 0
        i = 0
        j = len(people) - 1

        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1

        return ans
