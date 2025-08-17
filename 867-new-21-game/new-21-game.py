class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        l = [0.0] * maxPts
        l[0] = 1.0
        s = 1.0
        a = 0.0
        for i in range(1, n + 1):
            p = s / maxPts
            if i < k:
                s += p
            else:
                a += p
            if i >= maxPts:
                s -= l[i % maxPts]
            l[i % maxPts] = p
        return a