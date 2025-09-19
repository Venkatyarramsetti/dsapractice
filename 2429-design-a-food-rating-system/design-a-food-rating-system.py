import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d1 = {}  
        self.d2 = {}  
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.d1[food] = (cuisine, rating)
            if cuisine not in self.d2:
                self.d2[cuisine] = []
            heapq.heappush(self.d2[cuisine], (-rating, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.d1[food]
        self.d1[food] = (cuisine, newRating)
        heapq.heappush(self.d2[cuisine], (-newRating, food))       

    def highestRated(self, cuisine: str) -> str:
        heap = self.d2[cuisine]
        while heap:
            ra, food = heap[0]
            if self.d1[food][1] == -ra:
                return food
            heapq.heappop(heap)  
        return "" 


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)