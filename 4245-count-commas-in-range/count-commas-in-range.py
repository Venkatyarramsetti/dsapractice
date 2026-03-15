class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        c = 0
        for i in range(1000,n+1):
            c += 1
        return c