import collections
class Solution:
    # 先分類text與target，變成map模式，再迴圈target，把有在text的數量給減掉，如果其中一個字母不足數量，則直接return。
    # target迴圈完之後，就代表可以組成一個target。
    def maxNumberOfBalloons(self, text: str) -> int:
        cnts = collections.Counter(text)
        target = collections.Counter("balloon")

        ans = 0

        while True:
            for key in target:
                if key not in cnts:
                    return 0

                if target[key] <= cnts[key]:
                    cnts[key] -= target[key]
                else:
                    return ans

            ans += 1

        return ans


    def maxNumberOfBalloons_my(self, text: str) -> int:
        
        result = 9999999999

        balloonMap = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for c in text:
            if c in "balloon":
                balloonMap[c] += 1
                    

        balloonMap["l"] //= 2
        balloonMap["o"] //= 2

        for key in balloonMap.keys():
            if balloonMap[key] < result:
                result = balloonMap[key]
        return result


Solution.maxNumberOfBalloons(Solution(), "nlaebolko")