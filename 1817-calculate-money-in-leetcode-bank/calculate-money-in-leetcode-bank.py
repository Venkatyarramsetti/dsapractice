class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        d = n % 7
        c = 0
        for i in range(w):
            c += 7 * (i + 4)
        c += d * (w + 1) + d * (d - 1) // 2
        return c
