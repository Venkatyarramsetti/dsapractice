class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        u = [False] * n     
        c = 0 
        for fruit in fruits:
            placed = False
            for j in range(n):
                if not u[j] and baskets[j] >= fruit:
                    u[j] = True
                    placed = True
                    break
            if not placed:
                c += 1
        
        return c