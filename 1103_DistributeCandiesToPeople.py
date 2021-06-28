class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:

        result = [0] * num_people

        nowGive = 1
        giveIndex = 0

        while candies > 0:
            people = giveIndex % num_people

            result[people] = result[people] + nowGive
            
            candies -= nowGive
            nowGive += 1

            if nowGive > candies:
                nowGive = candies
            giveIndex += 1
        return result

Solution.distributeCandies(Solution(), 7, 4)