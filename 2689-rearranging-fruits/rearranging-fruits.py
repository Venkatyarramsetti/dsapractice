class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        f = Counter(basket1)
        for x in basket2: f[x] -= 1
        l = []
        for k, v in f.items():
            if v % 2 != 0:
                return -1
            l += [k] * abs(v // 2)
        minx = min(basket1 + basket2)
        l.sort()
        return sum(min(2*minx, x) for x in l[0:len(l)//2])