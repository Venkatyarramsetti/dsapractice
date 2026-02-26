class Solution:
    def numSteps(self, s: str) -> int:
        c = 0
        n = int(s,2)
        f = True
        while f:
            if n == 1:
                f = False
            elif n %2==0:
                n //=2
                c += 1
            elif n % 2 != 0:
                n += 1
                c += 1
        return c
