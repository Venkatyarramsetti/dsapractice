class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        f = Counter(costs)
        c = 0
        for i in range(1, max(f) + 1):
            buy = min(f[i], coins // i)
            c += buy
            coins -= buy * i
        return c