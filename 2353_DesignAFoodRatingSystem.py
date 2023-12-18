from collections import defaultdict
# from sortedcontainers import SortedSet
from sortedcontainers import SortedList
import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foodRatingMap = defaultdict(str)
        self.foodCuisineMap = defaultdict(str)
        self.cuisineFoodMap = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.foodRatingMap[f] = -r
            self.foodCuisineMap[f] = c
            heapq.heappush(self.cuisineFoodMap[c], (-r, f))

        
    def changeRating(self, food, newRating):

        self.foodRatingMap[food] = -newRating
        
        heapq.heappush(self.cuisineFoodMap[self.foodCuisineMap[food]], (-newRating, food))
    
    def highestRated(self, cuisine) -> str:
        
        r, f = self.cuisineFoodMap[cuisine][0]
        while r != self.foodRatingMap[f]:
            heapq.heappop(self.cuisineFoodMap[cuisine])
            r, f = self.cuisineFoodMap[cuisine][0]
        return f
    
class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_rating_map = defaultdict(int)
        self.food_cuisine_map = defaultdict(str)
        self.cuisine_food_map = defaultdict(SortedSet)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_cuisine_map[f] = c
            self.food_rating_map[f] = -r
            self.cuisine_food_map[c].add((-r, f))

    def changeRating(self, food, newRating):
        c = self.food_cuisine_map[food]
        old = (self.food_rating_map[food], food)
        new = (-newRating, food)
        self.food_rating_map[food] = -newRating
        self.cuisine_food_map[c].remove(old)
        self.cuisine_food_map[c].add(new)
    
    def highestRated(self, cuisine) -> str:
        return self.cuisine_food_map[cuisine][0][1]
    
fr = FoodRatings([["kimchi","miso","sushi","moussaka","ramen","bulgogi"],
                  ["korean","japanese","japanese","greek","japanese","korean"],
                  [9,12,8,15,14,7]])

print(fr.highestRated("korean"))
print(fr.highestRated("japanese"))
fr.changeRating("sushi", 16)
print(fr.highestRated("japanese"))
fr.changeRating("ramen", 16)
print(fr.highestRated("japanese"))

