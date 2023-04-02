class Solution:

    # def bs(self, target: int, )
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        ans = []
        potions.sort()
        count = len(potions)

        for n in spells:
            # n * potions >= success
            minmumPotion = success // n
            if success % n:
                minmumPotion += 1

            if potions[-1] < minmumPotion:
                ans.append(0)
                continue
            
            if potions[0] >= minmumPotion:
                ans.append(count)
                continue

            left = 0
            right = count - 1
            while left < right:

                mid = left + (right - left) // 2
                if potions[mid] > minmumPotion:
                    right = mid
                else:
                    left = mid+1
            
            print(minmumPotion, left, right)
                
            ans.append(count - left+1)

        return ans
        


